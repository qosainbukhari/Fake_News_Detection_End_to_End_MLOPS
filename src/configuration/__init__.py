from src.constant import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.utils import read_yaml, create_directories
from src.entity import (
    DataIngestionConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
)
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config["artifacts_root"]])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        create_directories([config["root_dir"]])
        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_url=config["source_url"],
            raw_data_dir=Path(config["raw_data_dir"]),
            local_data_file=Path(config["local_data_file"]),
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config["data_transformation"]
        create_directories([config["root_dir"]])
        return DataTransformationConfig(
            root_dir=Path(config["root_dir"]),
            data_path=Path(config["data_path"]),
            transformed_train_path=Path(config["transformed_train_path"]),
            transformed_test_path=Path(config["transformed_test_path"]),
        )

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config["model_trainer"]
        create_directories([config["root_dir"]])
        return ModelTrainerConfig(
            root_dir=Path(config["root_dir"]),
            train_data_path=Path(config["train_data_path"]),
            test_data_path=Path(config["test_data_path"]),
            model_path=Path(config["model_path"]),
            vectorizer_path=Path(config["vectorizer_path"]),
        )

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config["model_evaluation"]
        create_directories([config["root_dir"]])
        return ModelEvaluationConfig(
            root_dir=Path(config["root_dir"]),
            model_path=Path(config["model_path"]),
            test_data_path=Path(config["test_data_path"]),
            metric_file_path=Path(config["metric_file_path"]),
        )
