import sys
import json
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.logger import logger
from src.exception import CustomException
from src.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def initiate_model_evaluation(self):
        try:
            logger.info("Model evaluation started")

            test_df = pd.read_csv(self.config.test_data_path)
            X_test = test_df["content"].fillna("")
            y_test = test_df["label"]

            # Load model and vectorizer
            model = joblib.load(self.config.model_path)
            vectorizer_path = str(self.config.model_path).replace(
                "model.joblib", "tfidf_vectorizer.joblib"
            )
            tfidf = joblib.load(vectorizer_path)

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

            # Save metrics
            with open(self.config.metric_file_path, "w") as f:
                json.dump(metrics, f, indent=4)
            logger.info(f"Metrics saved at: {self.config.metric_file_path}")

            logger.info("Model evaluation completed")
            return metrics

        except Exception as e:
            raise CustomException(e, sys)
