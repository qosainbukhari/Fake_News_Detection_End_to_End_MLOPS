import os
import yaml
import json
import joblib
from pathlib import Path
from ensure import ensure_annotations
from src.logger import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file loaded from: {path_to_yaml}")
        return content


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> dict:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded from: {path}")
    return content


@ensure_annotations
def save_model(path: Path, model):
    joblib.dump(model, path)
    logger.info(f"Model saved at: {path}")


@ensure_annotations
def load_model(path: Path):
    model = joblib.load(path)
    logger.info(f"Model loaded from: {path}")
    return model
