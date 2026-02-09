from src.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src.logger import logger


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        params = config.params
        model_trainer = ModelTrainer(
            config=model_trainer_config, params=params
        )
        model_trainer.initiate_model_training()


if __name__ == "__main__":
    try:
        logger.info(">>> Model Trainer Pipeline started <<<")
        pipeline = ModelTrainerPipeline()
        pipeline.run()
        logger.info(">>> Model Trainer Pipeline completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e
