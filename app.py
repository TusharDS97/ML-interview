from src.EV_Market_Analysis.logger import logging
from src.EV_Market_Analysis.exception import CustomException
from src.EV_Market_Analysis.components.data_ingestion import DataIngestionConfig
from src.EV_Market_Analysis.components.data_ingestion import DataIngestion
import sys
if __name__ == "__main__":
    logging.info("Logging has started for EV Market Analysis")
    
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception has been raised")
        raise CustomException(e,sys)  