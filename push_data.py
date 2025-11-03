import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGODB_URI = os.getenv("MONGO_DB_URI")
print(f"MONGODB_URI: {MONGODB_URI}")

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.Exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract:
    def __init__(self, mongo_uri=MONGODB_URI):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    # ...existing code...

    def insert_data_mongoDB(self,records,database,collection_name):
        try:
            self.database = database
            self.collection_name = collection_name
            self.records = records

        # Add SSL certificate verification
            self.mongo_client = pymongo.MongoClient(
                MONGODB_URI,
                serverSelectionTimeoutMS=5000,
                ssl=True,
                ssl_cert_reqs='CERT_NONE'
                 )
        

    
        except Exception as e:
            raise NetworkSecurityException(e, sys)

# ...existing code...
        
if __name__=="__main__":
    try:
        FILE_PATH="Network_Data/phisingData.csv"
        DATABASE="SWANAND_DB"
        Collection="NETWORK_DATA"
        networkobj=NetworkDataExtract()
        records=networkobj.csv_to_json(file_path=FILE_PATH)
        print(records)
        no_of_records=networkobj.insert_data_mongoDB(records,DATABASE,Collection)
        print(f"No of records inserted: {no_of_records}")
    except Exception as e:
        raise NetworkSecurityException(e, sys)