import logging
import boto3
import sys
import pandas as pd


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

def get_job_id(job_name: str, file_path: str) -> int:
    """Retrieve or assign a unique job ID based on the job title.

    Args:
        job_name (str): The name of the job to retrieve or create an ID for.
        file_path (str): Path to the CSV file containing job categories.

    Returns:
        int: The job ID.
    """
    job_id_db = pd.read_csv(file_path)
    
    if not (job_id_db['job_title'].eq(job_name)).any():  # If the job title doesn't exist in job_categories.csv
        new_job_id = len(job_id_db)  # Assign the next ID
        new_data = pd.DataFrame({'job_id': [new_job_id], 'job_title': [job_name]})
        job_id_db = pd.concat([job_id_db, new_data], ignore_index=True)
        job_id_db.to_csv(file_path, index=False)  # Save the updated list
        return new_job_id
    else:
        # Return existing ID for the job title
        return job_id_db.loc[job_id_db['job_title'] == job_name, 'job_id'].iloc[0]
    

# Indeed Job Information Linking Table
def main():
    ## @params: [JOB_NAME]
    args = getResolvedOptions(sys.argv, ['JOB_NAME',
                                        'RAW_PROCESSED',
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
    raw_processed_layer = args['RAW_PROCESSED']
    s3_output = args['S3_OUTPUT']
    indeed_artifacts_bucket = args['ARTIFACTS_BUCKET']
    indeed_databucket_name = (str(raw_processed_layer).split('/'))[2] ## Extracts Indeed Pipeline Bucket Name from S3://bucket_name/folder Parameter S3_INPUT
    job_category_file = indeed_artifacts_bucket + r"dependencies/job_categories.csv"
    
    # Create Boto3 Resources For Looping
    s3 = boto3.resource("s3")
    s3_bucket = s3.Bucket(indeed_databucket_name) 
    raw_processed_folder = 'raw_processed/'
    
    # list of raw_processed layers csv files
    list_of_files =  [x for x in [f.key.split(raw_processed_folder)[1] for f in s3_bucket.objects.filter(Prefix=raw_processed_folder).all()] if x]
    
    # Create job_information curated folder
    create_curated_folder(indeed_databucket_name, 'job_information', logger)
    
    # Loop thorough raw_processed layer, append to empty dataframe, call job_categories to assign ids to combined raw_processed dataframe object
    columns = ["numb_description", "job_description", "state", "report_year", "job_id"] 
    combined_df = pd.DataFrame(columns=columns) # empty dataframe object
    try:
        for filename in list_of_files: 
            dataframe = pd.read_csv(raw_processed_layer + filename)
            job_title = filename.split("_")[0] # get job id based on file name
            job_id = get_job_id(job_title, job_category_file)
            dataframe['job_id'] = job_id
            combined_df = pd.concat([combined_df, dataframe], ignore_index=True) # append to empty dataframe object

    except Exception as e:
        logger.error("Cannot read to target s3 location " + raw_processed_layer + ": {}".format(e))
        sys.exit(1)
        
    # Convert raw_processed pandas db to spark db, read job_categories mapping csv
    try: 
        spark_raw_processed_df = spark.createDataFrame(combined_df) # convert pandas df to spark df
        job_categories = spark.read.option("header", True).option("inferSchema", True).csv(job_category_file)

        spark_raw_processed_df.createOrReplaceTempView("raw_processed_db") 
        job_categories.createOrReplaceTempView("job_categories") 

    except Exception as e:
        logger.error("Cannot read to target s3 location " + raw_processed_layer + ": {}".format(e))
        sys.exit(2)

    
    # Join Linking Table with Education Layer to extract job sample size (universal count via all tables)
    result_df = spark.sql('''
            SELECT jc.job_id,
                jc.job_title,
                COUNT(*) AS total_job_descriptions,
                rp.state,
                rp.report_year
            FROM job_categories jc
            LEFT JOIN raw_processed_db rp
                ON jc.job_id = rp.job_id
            GROUP BY jc.job_id, jc.job_title, rp.state, rp.report_year
            ORDER BY jc.job_id ASC, rp.report_year DESC
        ''')

    # Partition Columns
    partitional_cols = ["report_year"]

    # Write Dataframe Into Curated Education Folder
    try:
        result_df.write.mode("overwrite").partitionBy(*partitional_cols).format("parquet").save(s3_output)

    except Exception as e:
        logger.error("Cannot write to target s3 location " + s3_output + ": {}".format(e))
        sys.exit(3)


# Run Main Function
main() 