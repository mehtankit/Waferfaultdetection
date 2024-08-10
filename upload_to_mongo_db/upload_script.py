from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri= "mongodb+srv://lowkeyankit:lilnugget@cluster0.pifn1nu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

DATABASE_NAME = "WaferFaultDetection"
COLLECTION_NAME = "wafer_fault_data"


df = pd.read_csv(r"D:\Projects\Project\Waferfault\notebook\data\wafer.csv")
df = df.drop(columns=["Unnamed: 0"])

json_data = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_data)