# (Read the data and split the data, Data is extracted from the various source like Db - Mysql, Monogo etc)

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass                           #Decorator- used to create a class shortly, and also used to define the class variable directly without init

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('E:/New folder/Student-Performance-Analysis/notebook-files/data/StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')

            # Define the column rename mapping
            rename_mapping = {
                "gender": "gender",
                "race/ethnicity": "race_ethnicity",
                "parental level of education": "parental_level_of_education",
                "lunch": "lunch",
                "test preparation course": "test_preparation_course",
                "math score": "math_score",
                "reading score": "reading_score",
                "writing score": "writing_score"
            }

            # Rename columns in the dataframe
            df.rename(columns=rename_mapping, inplace=True)
            logging.info("Column headers renamed")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)          #Raw data

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) #Train Data

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)   #Test Data

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))