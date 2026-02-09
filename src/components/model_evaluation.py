import sys
import json
import pandas as pd
import joblib
import mlflow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.logger import logger
from src.exception import CustomException
from src.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig, params: dict):
        self.config = config
        self.params = params

    def initiate_model_evaluation(self):
        try:
            logger.info("Model evaluation started")

            test_df = pd.read_csv(self.config.test_data_path)
            X_test = test_df["content"].fillna("")
            y_test = test_df["label"]

            # Load model and vectorizer
            model = joblib.load(self.config.model_path)
            tfidf = joblib.load(self.config.vectorizer_path)

            X_test_tfidf = tfidf.transform(X_test)
            y_pred = model.predict(X_test_tfidf)

            # Calculate metrics
            metrics = {
                "accuracy": round(accuracy_score(y_test, y_pred), 4),
                "precision": round(precision_score(y_test, y_pred), 4),
                "recall": round(recall_score(y_test, y_pred), 4),
                "f1_score": round(f1_score(y_test, y_pred), 4),
            }

            logger.info(f"Metrics: {metrics}")

            # Save metrics to JSON
            with open(self.config.metric_file_path, "w") as f:
                json.dump(metrics, f, indent=4)
            logger.info(f"Metrics saved at: {self.config.metric_file_path}")

            # MLflow tracking
            mlflow.set_tracking_uri(self.config.mlflow_uri)
            mlflow.set_experiment(self.config.experiment_name)

            with mlflow.start_run():
                # Log parameters
                mlflow.log_param("model_name", self.params["model"]["name"])
                mlflow.log_param("max_features", self.params["max_features"])
                mlflow.log_param("test_size", self.params["test_size"])
                for key, value in self.params["model"]["params"].items():
                    mlflow.log_param(key, value)

                # Log metrics
                for key, value in metrics.items():
                    mlflow.log_metric(key, value)

                # Log model
                mlflow.sklearn.log_model(model, "model")

                logger.info("MLflow tracking completed")

            logger.info("Model evaluation completed")
            return metrics

        except Exception as e:
            raise CustomException(e, sys)
