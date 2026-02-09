import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from src.logger import logger
from src.exception import CustomException
from src.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig, params: dict):
        self.config = config
        self.params = params

    def initiate_model_training(self):
        try:
            logger.info("Model training started")

            train_df = pd.read_csv(self.config.train_data_path)
            test_df = pd.read_csv(self.config.test_data_path)

            X_train = train_df["content"].fillna("")
            y_train = train_df["label"]
            X_test = test_df["content"].fillna("")
            y_test = test_df["label"]

            logger.info(f"Train: {X_train.shape[0]}, Test: {X_test.shape[0]}")

            # TF-IDF Vectorization
            tfidf = TfidfVectorizer(
                max_features=self.params["max_features"]
            )
            X_train_tfidf = tfidf.fit_transform(X_train)
            X_test_tfidf = tfidf.transform(X_test)
            logger.info(f"TF-IDF shape: {X_train_tfidf.shape}")

            # Train Random Forest
            model_params = self.params["model"]["params"]
            model = RandomForestClassifier(**model_params)
            model.fit(X_train_tfidf, y_train)
            logger.info("Model training completed")

            # Save model and vectorizer
            joblib.dump(model, self.config.model_path)
            logger.info(f"Model saved at: {self.config.model_path}")

            joblib.dump(tfidf, self.config.vectorizer_path)
            logger.info(f"Vectorizer saved at: {self.config.vectorizer_path}")

        except Exception as e:
            raise CustomException(e, sys)
