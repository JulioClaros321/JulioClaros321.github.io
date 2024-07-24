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

# Indeed Salary Curated Job
def main():
    ## @params: [JOB_NAME]
    args = getResolvedOptions(sys.argv, ['JOB_NAME',
                                        'S3_INPUT',
                                        'S3_OUTPUT'])

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
    indeed_databucket_name = (str(s3_input).split('/'))[2] ## Extracts Indeed Pipeline Bucket Name 
    # Create salary curated folder
    create_curated_folder(indeed_databucket_name, 'salary', logger)

    # Read cleansed salary folder, sys.exit if error
    try: 
        salary_db = spark.read.option("header", True).option("inferSchema", True).csv(s3_input)
        salary_db.createOrReplaceTempView('salary_db')

    except Exception as e:
        logger.error("Cannot read to target s3 location " + s3_input + ": {}".format(e))
        sys.exit(1)

    # Group frequency counts via pyspark.sql
    result_df = spark.sql("""
                        SELECT job_id,
                               pay_low_end AS low_end_salary, 
                               pay_high_end AS high_end_salary, 
                               state, 
                               report_year
                        FROM salary_db 
                        ORDER BY pay_low_end ASC
                      """
                     )
    
    # Partition Columns
    partitional_cols = ["report_year"]

    # Write result dataframe to salary curated folder
    try:
        result_df.write.mode("overwrite").partitionBy(*partitional_cols).format("parquet").save(s3_output)

    except Exception as e:
        logger.error("Cannot write to target s3 location " + s3_output + ": {}".format(e))
        sys.exit(2)


# Run Main Function
main()
