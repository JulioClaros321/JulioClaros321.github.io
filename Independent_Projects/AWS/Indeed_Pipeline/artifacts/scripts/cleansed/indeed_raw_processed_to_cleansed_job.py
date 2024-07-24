import pandas as pd 
import csv
import os 
import re
import sys
import copy
import boto3, logging

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job



def read_csv_from_s3(bucket, key):
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    return pd.read_csv(obj['Body'])

def create_dictionary_from_csv(path_to_csv: str) -> dict:
    ''' Creates environment folders and partitioning folders when new job title is created 
        Args: 
        path_to_csv (str): string path to csv file needed to make a frequency dictionary
        Returns:
        freq_dictionary (dict): blank frequency dictionary '''
    
    freq_dictionary = {} 
    bucket, key = path_to_csv.replace("s3://", "").split("/", 1)
    df = read_csv_from_s3(bucket, key)

    for row in df.itertuples(index=False):
        freq_dictionary[row[0]] = 0
    
    return freq_dictionary

def create_cleansed_environment(bucket_name: str, list_of_files_in_raw: list, output_folder: str, logger: object) -> list:
    ''' Creates cleansed environment folders and partitioning folders when new job title is created, and returns a list of unique job titles to order the files processed by job_title 
    
        Args:
        bucket_name (str): bucket name string
        list_of_files_in_raw (list): list of all files collected using os.listdir
        output_folder (str): job s3 output folder path
        logger (str): logger object for outputs and debugging
        
        Returns:
        all_job_names (list): list of all unique names collected from raw files listed'''
        
    s3 = boto3.client('s3')  
    partition_folders = ['education', 'programming_languages', 'personality_traits', 'skillset', 'software', 'security_clearance', 'experience', 'salary']
    all_job_names = []
    
    for word_docx_filename in list_of_files_in_raw:
        position_title = word_docx_filename.split('_')[0]
        if position_title not in all_job_names:
            all_job_names.append(position_title)
            
    for folder in partition_folders:
        prefix = "cleansed/" + folder + "/"
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
        
        if 'Contents' in response:
            # Folder exists
            logger.info(folder + " folder exists and code will begin executing")
        else:
            logger.info(folder + " folder not found, will add it now")   
            s3.put_object(Bucket=bucket_name, Key=prefix)

        
    return all_job_names

def extract_salary_from_paragraph(job_id: int, output_folder: str, word_docx_filename: str, document_to_string: str):
    ''' Uses regex to capture salary for positions patterns and writes them into a dataframe object
        
        Args:
        job_id (int): job titlte unique identifier
        salary_tuple: tuple of low end, high end, and hourly/salary pay grades
        word_docx_filename (str): name of file being processed 
        document_to_string (str): job descriptions joined into a string object for processing
        
        Returns: 
        Tuple: a tuple of job low/high end pay ranges '''
    file_name_split = word_docx_filename.split('_')
    state = file_name_split[1]
    report_year = file_name_split[2].split('-')[0]
    
    salary_tuple = re.findall(r'(\$?\d{1,3}(?:k|,\d{1,3}|\d{1,3}))\s*?(?:to|-)\s*?(\$?\d{1,3}(?:k|,\d{1,3}|\d{1,3}))(?:\s*(?:per\s+|a\s+)?(hour|annually|year|yearly))?', document_to_string)
    pattern = r'[^a-zA-Z0-9\s]' # remove special characters
    low_end_pay = [] 
    high_end_pay = [] 
    
    
    for matches in salary_tuple: 
        low = re.sub(pattern, '', matches[0]) # remove special characters
        high = re.sub(pattern, '', matches[1]) # remove special characters
        
        low = re.sub('k', '000', low) # replace k with 000
        high = re.sub('k', '000', high) 
        
        
        if int(low) < 20000 or int(high) < 20000:
            
            if matches[2] == 'year' or matches[2] == 'annually':
                
                if len(low) < 5: low = int(low) * 1000
                if len(high) < 5: high = int(high) * 1000
                
                if int(low) < 20000 or int(high) < 20000:
                    continue
                    
            elif matches[2] == 'hour' or matches[2] == 'hourly':
                low = int(low) * 40 * 52 # Convert to salary
                high = int(high) * 40 * 52 # Convert to salary
                
            else: 
                continue
        
        low_end_pay.append(int(low))
        high_end_pay.append(int(high))
        
    salary_dataframe = pd.DataFrame()
    salary_dataframe['pay_low_end'] = low_end_pay
    salary_dataframe['pay_high_end'] = high_end_pay
    salary_dataframe['job_id'] = job_id
    salary_dataframe['state'] = state
    salary_dataframe['report_year'] = report_year
    
    salary_dataframe.to_csv(output_folder + 'salary' + "/" + word_docx_filename + '.csv', index=False)

def extract_experience_from_paragraph(job_id: str, output_folder: str, word_docx_filename: str, document_to_string: str):
    """ Function uses regex to find experience requirements within job descriptions and writes all experience patterns captured into a dataframe object
    
    Args:
    job_id: unique identifier for job
    output_folder (str): s3 path for output file (cleansed folder)
    word_docx_filename (str): name of file being processed
    document_to_string (str): job descriptions joined into string object for processing
    
    """
    file_name_split = word_docx_filename.split('_')
    state = file_name_split[1]
    report_year = file_name_split[2].split('-')[0]
    
    years_experience = []
    list_of_experience = re.findall(re.compile(r'(\d+\+?|\d+\s*[-–to]\s*\d+)\s*(years?)'), document_to_string)
    
    for items in list_of_experience:
        years = re.sub(r'[^a-zA-Z0-9-]', '', items[0])
        
        if '-' in years: 
            years_array = years.split('-') 
            ranged_item = list(range(int(years_array[0]), int(years_array[1]) + 1))
            years_experience.extend(ranged_item)
        elif int(years) > 15: 
            continue
        else: years_experience.append(int(years))
    
    experience_db = pd.DataFrame()
    experience_db['years_experience_recorded'] = years_experience
    experience_db['job_id'] = job_id
    experience_db['state'] = state
    experience_db['report_year'] = report_year
    
    experience_db.to_csv(output_folder + 'experience' + "/" + word_docx_filename + '.csv', index=False)

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

def write_dictionary_to_cleansed_layer(measurement_dictionary: dict, job_id: str, output_folder: str, folder: str, file_name: str): 
    """Write creates a dataframe object from dictionary passed, and writes it into a csv with the same file name
    
    Args:
    measurement_dictionary (dict): frequency dictionary.
    job_id (int): unique job id.
    output_folder (str): path to cleansed layer.
    folder (str): job specific folder in cleansed layer.
    word_docx_filename (str): name of file being used
    """
    
    file_name_split = file_name.split('_')
    state = file_name_split[1]
    report_year = file_name_split[2].split('-')[0]
    
    for name, dictionary in measurement_dictionary.items():
        
        dataframe = pd.DataFrame(list(measurement_dictionary.items()), columns = [folder, 'frequency'])
        dataframe['job_id'] = job_id  # Adding job_id column
        dataframe['state'] = state  # Adding state column
        dataframe['report_year'] = report_year  # Adding report year column
        dataframe.to_csv(output_folder + folder + "/" + file_name + '.csv', index=False)

def mark_phrases(word_doc_text: str, words_for_marking_desc: list) -> str:
    ''' Function takes multiple worded phrases from dictionaries and replaced space with '-' in order to mark them before counting 
        
        Args: 
        word_doc_text (str): word documented converted into a string 
        words_for_marking (list) : list of phrases that will be marked to count accurately 
        
        Returns: 
        word_doc_text (str): word document with marked text '''
    for phrase in words_for_marking_desc:

        word_doc_text = re.sub(phrase, phrase.replace(' ', '-'), word_doc_text)
        
    return word_doc_text

def find_special_characters(s: str):
    '''
    Function removes non-alphanumeric characters
    
    Args: 
    s (str): text based value 
    
    Returns: 
    s (str): cleaned text 
    
    '''
    # This pattern matches any character that is not a letter or a number
    pattern = re.compile('[^a-zA-Z0-9]')
    # Find all non-alphanumeric characters in the string
    special_chars = pattern.findall(s)
    unique_special_chars = set(special_chars)
    
    for special_character in unique_special_chars: 
        s = s.replace(special_character, "\\" + special_character)
    return s

def create_key_glossary_from_dict_shells(bucket, dictionary_skeletons_folder):
    glossary_path = dictionary_skeletons_folder + 'dict_key_glossary.csv'
    bucket_name = bucket.split('/')[2]
    # Check if the glossary file exists
    try:
        glossary_db = read_csv_from_s3(bucket_name, glossary_path)
    except:
        glossary_db = pd.DataFrame(columns=['keys'])
        
        # List all files in the dictionary skeletons folder
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=dictionary_skeletons_folder)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                file_key = obj['Key']
                if file_key.endswith('.csv'):
                    keyword_list = read_csv_from_s3(bucket, file_key).iloc[:, 0].tolist()
                    new_df = pd.DataFrame(keyword_list, columns=['keys'])
                    glossary_db = pd.concat([glossary_db, new_df], ignore_index=True)
        
        # Save the glossary back to S3
        csv_buffer = StringIO()
        glossary_db.to_csv(csv_buffer, index=False)
        s3.put_object(Bucket=bucket, Key=glossary_path, Body=csv_buffer.getvalue())
        
    list_of_hypend_words = [x for x in glossary_db.iloc[:, 0].tolist() if "-" in x]
    words_without_hyphens = list(map(lambda word: word.replace('-', ' '), list_of_hypend_words))
    words_without_hyphens_desc = sorted(words_without_hyphens, key=len, reverse=True)
    
    return words_without_hyphens_desc
    
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
    s3_artifacts_folder = args['ARTIFACTS_BUCKET']
    
    indeed_bucket_name = str(s3_input).split('//')[1].split('/')[0] # Extract databucket name (s3://{databucket}/raw_processed)
    s3 = boto3.resource("s3") # boto3 resources
    s3_bucket = s3.Bucket(indeed_bucket_name) 
    raw_processed_folder = 'raw_processed/'
    
    job_category_folder = str(s3_artifacts_folder) + r"dependencies/job_categories.csv"
    dictionary_skeletons_folder = str(s3_artifacts_folder) + r"dictionary_shells/"

    # Pre-load dictionary shells
    dictionary_shells = {
        "education": create_dictionary_from_csv(os.path.join(dictionary_skeletons_folder + "education.csv")),
        "programming_languages": create_dictionary_from_csv(os.path.join(dictionary_skeletons_folder, "programming_languages.csv")),
        "personality_traits": create_dictionary_from_csv(os.path.join(dictionary_skeletons_folder, "personality_traits.csv")),
        "skills": create_dictionary_from_csv(os.path.join(dictionary_skeletons_folder, "skills.csv")),
        "software": create_dictionary_from_csv(os.path.join(dictionary_skeletons_folder, "software.csv")),
        "security_clearance": create_dictionary_from_csv(os.path.join(dictionary_skeletons_folder, "security_clearance.csv"))
    }
    # Create list of words and phrases for frequency counter
    words_for_marking_desc = create_key_glossary_from_dict_shells(s3_artifacts_folder, r"dictionary_shells/")

    # Get list of files and create cleansed folders
    list_of_files =  [x for x in [f.key.split(raw_processed_folder)[1] for f in s3_bucket.objects.filter(Prefix=raw_processed_folder).all()] if x]
    unique_job_names = create_cleansed_environment(indeed_bucket_name, list_of_files, s3_output, logger)

    # Loop through csv files in raw_processed folder
    for job_title in unique_job_names:

        # Get job unique identifier or create one
        job_id = get_job_id(job_title, job_category_folder)

        # Sort files based on job_title naming convention
        job_specific_files = [x for x in list_of_files if job_title in x]
        
        # Loop through job_name specific files
        for filename in job_specific_files:
            # Processed job_description column from csv and create a string object
            job_desc_db = pd.read_csv(s3_input + filename)
            job_descriptions_list = job_desc_db['job_description'].tolist()
            job_descriptions_string = ' '.join(job_descriptions_list)
            
            # Mark phrases in string object (exp.): masters degree => masters-degree. 
            document_to_string_v2 = mark_phrases(job_descriptions_string, words_for_marking_desc)

            # Extract experience requirements within job descriptions
            extract_experience_from_paragraph(job_id, s3_output, filename, document_to_string_v2)
            
            # Extract salary offers within job descriptions
            extract_salary_from_paragraph(job_id, s3_output, filename, document_to_string_v2)

            # Reset frequency dictionaries to initial template by deep copying
            dictionaries = {k: copy.deepcopy(v) for k, v in dictionary_shells.items()}
            
            # Declare partition folders
            partition_folders = ['education', 'programming_languages', 'personality_traits', 'skillset', 'software', 'security_clearance']

            # Dictionary frequency counter
            counter = 0
            for counter, (category, dictionary) in enumerate(dictionaries.items()):
                for key in dictionary:
                    regex_key = find_special_characters(key)
                    pattern = r"(?<=\s)[\.,(]*" + regex_key + r"[\.,)]*(?=\s)"
                    dictionary[key] = len(re.findall(pattern, document_to_string_v2))
                write_dictionary_to_cleansed_layer(dictionary, job_id, s3_output, partition_folders[counter], filename)
                counter += 1




# Run Main Loop
main()