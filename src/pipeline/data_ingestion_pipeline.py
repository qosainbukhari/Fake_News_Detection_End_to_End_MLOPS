from src.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logger import logger


class DataIngestionPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.initiate_data_ingestion()


if __name__ == "__main__":
    try:
        logger.info(">>> Data Ingestion Pipeline started <<<")
        pipeline = DataIngestionPipeline()
        pipeline.run()
        logger.info(">>> Data Ingestion Pipeline completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e
