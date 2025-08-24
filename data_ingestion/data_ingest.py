import langchain_astradb
from dotenv import load_dotenv
import os
import pandas as pd
from data_ingestion.data_transform import data_converter


class ingest_data:
    def __init__(self):
        pass
    
    
    def data_ingestion(self):
        print("Data ingestion started!")
    
    
if __name__ == '__main__':
    print("Running data_ingest.py...")
    
    data_ingestion=ingest_data()
    data_ingestion.data_ingestion()
    # your code heredata_ingestion = ingest_data()

