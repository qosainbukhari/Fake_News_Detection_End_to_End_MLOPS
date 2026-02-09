from src.logger import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion"
try:
    logger.info(f"========== {STAGE_NAME} started ==========")
    pipeline = DataIngestionPipeline()
    pipeline.run()
    logger.info(f"========== {STAGE_NAME} completed ==========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation"
try:
    logger.info(f"========== {STAGE_NAME} started ==========")
    pipeline = DataTransformationPipeline()
    pipeline.run()
    logger.info(f"========== {STAGE_NAME} completed ==========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training"
try:
    logger.info(f"========== {STAGE_NAME} started ==========")
    pipeline = ModelTrainerPipeline()
    pipeline.run()
    logger.info(f"========== {STAGE_NAME} completed ==========")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f"========== {STAGE_NAME} started ==========")
    pipeline = ModelEvaluationPipeline()
    pipeline.run()
    logger.info(f"========== {STAGE_NAME} completed ==========")
except Exception as e:
    logger.exception(e)
    raise e
