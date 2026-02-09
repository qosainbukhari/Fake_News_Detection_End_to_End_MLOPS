from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    raw_data_dir: Path
    local_data_file: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    transformed_train_path: Path
    transformed_test_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_path: Path
    vectorizer_path: Path


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    vectorizer_path: Path
    test_data_path: Path
    metric_file_path: Path
    mlflow_uri: str
    experiment_name: str
