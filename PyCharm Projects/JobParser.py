import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

page = requests.get("https://www.indeed.com/jobs?q=data+scientist+$20,000&l=Was"
                    "hington+DC&jt=internship&sort=date")

soup = BeautifulSoup(page.content, "html.parser")

job_name = []
company_name = []
city = []
description = []
dates = []



result = soup.findAll("div", "row")

date = soup.findAll(class_="date")

for items in date:
    date = items.text
    dates.append(date)



for res in result:
    sample = []
    text = res.text
    haha = text.replace(",", "")
    fixed_text = re.sub("\n+", ",", haha.strip())
    sample = fixed_text.split(",")

    job_name.append(sample[0])
    company_name.append(sample[1])
    city.append(sample[3])
    description.append(sample[4])



num_rows = len(job_name) + 1
row_list = list(range(1, num_rows))

indeed_jobs_df = pd.DataFrame({"Job_Name": job_name, "Company": company_name,
                "Location": city, "Description": description,
                "Posted": dates}, index= row_list)

indeed_jobs_df.to_csv(r"C:\Users\Julio\Downloads\Indeed_Jobs.csv", index=False)



