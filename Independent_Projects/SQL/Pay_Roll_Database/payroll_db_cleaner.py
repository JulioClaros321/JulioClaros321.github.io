import pandas as pd
import numpy as np
import mysql.connector


database = mysql.connector.connect(host="localhost", database ="payroll_db",
                             user="root", password="Immalegacy5")
employees = pd.read_csv("Employee_Dummy.csv")

print(employees.head())