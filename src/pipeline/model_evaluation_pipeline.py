from src.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logger import logger


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.initiate_model_evaluation()


if __name__ == "__main__":
    try:
        logger.info(">>> Model Evaluation Pipeline started <<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.run()
        logger.info(">>> Model Evaluation Pipeline completed <<<")
    except Exception as e:
        logger.exception(e)
        raise e
