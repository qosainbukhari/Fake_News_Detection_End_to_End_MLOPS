from src.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logger import logger


class DataTransformationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        params = config.params
        data_transformation = DataTransformation(
            config=data_transformation_config, params=params
        )
        data_transformation.initiate_data_transformation()


if __name__ == "__main__":
    try:
        logger.info(">>> Data Transformation Pipeline started <<<")
        pipeline = DataTransformationPipeline()
        pipeline.run()
        logger.info(">>> Data Transformation Pipeline completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e
