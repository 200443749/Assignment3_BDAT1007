from bs4 import BeautifulSoup
from textblob import TextBlob
import requests
import os
import pandas as pd
import csv
from pymongo import MongoClient

client = MongoClient("mongodb+srv://binay_99:Watson%4099@bdat1007.n5kgy.mongodb.net/test?authSource=admin&replicaSet=atlas-124cba-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db=client["sentimental_db"]
CBC_tbl=db["CBC_news"]
thestar_tbl=db["thestar_news"]
cbc_file='cbc.csv'
thestar_file='thestar.csv'
# CSV file to MongoDB
def csv_to_json(filename,header=None):
    data = pd.read_csv(filename, header=header)
    return data.to_dict('records')
CBC_tbl.insert_many(csv_to_json(cbc_file,header=0))
thestar_tbl.insert_many(csv_to_json(thestar_file,header=0))
