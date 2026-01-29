import os
import sys
from src.EV_Market_Analysis.exception import CustomException
from src.EV_Market_Analysis.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"D:\Internship\.env", override=True)

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
db = os.getenv("MYSQL_DB")


def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established",mydb)
        df = pd.read_sql_query("SELECT * FROM metals", mydb)
        print(df.head())
        
        return df
    except Exception as ex:
        raise CustomException(ex,sys)