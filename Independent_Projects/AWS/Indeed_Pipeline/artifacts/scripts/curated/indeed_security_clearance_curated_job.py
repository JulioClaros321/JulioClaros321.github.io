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

# Indeed Security Clearance Curated Job 
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
    indeed_databucket_name = (str(s3_input).split('/'))[2] ## Extracts Indeed Pipeline Bucket Name 
    skeletons_mapping_folder = indeed_artifacts_bucket + r"category_mapping/"
    
    # Create security_clearance curated folder
    create_curated_folder(indeed_databucket_name, 'security_clearance', logger)

    # Read cleansed security clearance cleansed/mapping folder 
    try: 
        security_clearance_db = spark.read.option("header", True).option("inferSchema", True).csv(s3_input)
        security_clearance_mapping = spark.read.option("header", True).option("inferSchema", True).csv(skeletons_mapping_folder + r"security_clearance_mapping.csv")

        security_clearance_db.createOrReplaceTempView("security_clearance_db")
        security_clearance_mapping.createOrReplaceTempView("security_clearance_mapping_db")

    except Exception as e:
        logger.error("Cannot read to target s3 location " + s3_input + ": {}".format(e))
        sys.exit(1)

    
    # Map database with mapping csv
    result_df = spark.sql("""
                        
                        SELECT scdb.job_id,
                               map.clearance_category, 
                               SUM(scdb.frequency) AS frequency,
                               scdb.state,
                               scdb.report_year
                               FROM security_clearance_db scdb
                                   LEFT JOIN security_clearance_mapping_db map 
                                   ON scdb.security_clearance = map.security_clearance
                               GROUP BY map.clearance_category, scdb.job_id, scdb.state, scdb.report_year
                               ORDER BY map.clearance_category ASC, scdb.job_id ASC, scdb.report_year DESC
                      """
                     )

    # Partition Columns
    partitional_cols = ["report_year"]

    # Write Dataframe Object Into Curated Security Clearance Folder 
    try:
        result_df.write.mode("overwrite").partitionBy(*partitional_cols).format("parquet").save(s3_output)

    except Exception as e:
        logger.error("Cannot write to target s3 location " + s3_output + ": {}".format(e))
        sys.exit(2)


# Run Main Function
main() 