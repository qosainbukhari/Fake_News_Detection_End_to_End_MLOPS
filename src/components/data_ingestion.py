import os
import shutil
import pandas as pd
from src.logger import logger
from src.exception import CustomException
from src.entity import DataIngestionConfig
import sys


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self) -> str:
        try:
            logger.info("Data ingestion started")

            # Read data from raw directory
            raw_file = os.path.join(
                self.config.raw_data_dir, "WELFake_Dataset.csv"
            )
            logger.info(f"Reading data from: {raw_file}")
            df = pd.read_csv(raw_file)

            logger.info(f"Dataset shape: {df.shape}")
            logger.info(f"Columns: {list(df.columns)}")

            # Save a copy to artifacts for pipeline use
            os.makedirs(
                os.path.dirname(self.config.local_data_file), exist_ok=True
            )
            df.to_csv(self.config.local_data_file, index=False)
            logger.info(
                f"Data saved to: {self.config.local_data_file}"
            )

            logger.info("Data ingestion completed")
            return str(self.config.local_data_file)

        except Exception as e:
            raise CustomException(e, sys)
