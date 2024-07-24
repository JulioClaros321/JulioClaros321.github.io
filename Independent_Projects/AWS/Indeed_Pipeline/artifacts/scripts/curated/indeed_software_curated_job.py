import logging
import boto3
import sys

from pyspark import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession

def create_curated_folder(bucket_name, folder_name, logger): 
    ## Creates Folder If It Does Not Already Exist In Curated Layer Before Job Is Called 
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix="curated/" + folder_name + "/")
    
    if 'Contents' in response:
        # Folder Exists
        logger.info(folder_name + " folder exists and code will begin executing")
    else:
        # Adds Folder 
        logger.info(folder_name + " folder not found, will add it now")   
        s3.put_object(Bucket=bucket_name, Key="curated/" + folder_name + "/")

# Indeed Software Curated Job 
def main():
    ## @params: [JOB_NAME]
    args = getResolvedOptions(sys.argv, ['JOB_NAME',
                                        'S3_INPUT',
                                        'S3_OUTPUT',
                                        'ARTIFACTS_BUCKET'])


    ## Logger Details 
    MSG_FORMAT = '%(asctime)s %(levelname)s %(name)s: %(message)s'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    logging.basicConfig(format=MSG_FORMAT, datefmt=DATETIME_FORMAT)
    logger = logging.getLogger('Console')
    logger.setLevel(logging.INFO)

    ## Establish Spark Session
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session
    job = Job(glueContext)

    ## Calls Parameters & Creates Variables
    job.init(args['JOB_NAME'], args)
    s3_input = args['S3_INPUT']
    s3_output = args['S3_OUTPUT']
    indeed_artifacts_bucket = args['ARTIFACTS_BUCKET']
    indeed_databucket_name = (str(s3_input).split('/'))[2] ## Extracts Indeed Pipeline Bucket Name from S3://headstart_bucketname/folder Parameter S3_INPUT
    skeletons_mapping_folder = indeed_artifacts_bucket + r"category_mapping/"
    
    # Create software curated folder
    create_curated_folder(indeed_databucket_name, 'software', logger)

    # Read software cleansed/mapping folder 
    try: 
        software_db = spark.read.option("header", True).option("inferSchema", True).csv(s3_input)
        software_map = spark.read.option("header", True).option("inferSchema", True).csv(skeletons_mapping_folder + r"software_category_mapping.csv")

        software_db.createOrReplaceTempView("software_db")
        software_map.createOrReplaceTempView("software_map")

    except Exception as e:
        logger.error("Cannot read to target s3 location " + s3_input + ": {}".format(e))
        sys.exit(1)

    
    # Map database with mapping csv
    result_df = spark.sql("""
                        SELECT sdb.job_id, 
                               sdb.software,
                               map.software_category, 
                               SUM(sdb.frequency) AS frequency, 
                               sdb.state, 
                               sdb.report_year 
                        FROM software_db sdb
                            LEFT JOIN software_map map 
                            ON sdb.software = map.software_name
                        GROUP BY sdb.software, sdb.job_id, map.software_category, sdb.state, sdb.report_year
                        ORDER BY map.software_category ASC, sdb.software ASC, sdb.job_id ASC, sdb.report_year ASC
                      """
                     )

    # Partition Columns
    partitional_cols = ["report_year"]

    # Write Dataframe Object Into Curated Software Folder
    try:
        result_df.write.mode("overwrite").partitionBy(*partitional_cols).format("parquet").save(s3_output)

    except Exception as e:
        logger.error("Cannot write to target s3 location " + s3_output + ": {}".format(e))
        sys.exit(2)


# Run Main Function
main() 