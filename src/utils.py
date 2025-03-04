import os
import sys
import pickle
import numpy as np 
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import f1_score

from pymongo import MongoClient

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = f1_score(ytrain,y_train_pred)
            test_model_score = f1_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report
    
    except Exception as e:
            logging.info('Exception occured during model training')
            raise CustomException(e,sys)
    

def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception Occured in load_object function utils')
        raise CustomException(e,sys)
    
def export_from_mongodb(collection_name, database_name):
    try:
        uri= "mongodb+srv://lowkeyankit:lilnugget@cluster0.pifn1nu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        collection = client[database_name][collection_name]

        df = pd.DataFrame(list(collection.find()))

        if "_id" in df.columns:
            df.drop(columns=["_id"], inplace=True, axis=1)
        
        df.replace('', np.nan, inplace=True)

        return df

    except Exception as e:
        logging.info('Exception occured during exporting data from mongodb')
        raise CustomException(e,sys)