import os
import sys
import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from src.logger import logger
from src.exception import CustomException
from src.entity import DataTransformationConfig

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig, params: dict):
        self.config = config
        self.params = params
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r"https?://\S+|www\.\S+", "", text)
        text = re.sub(r"<.*?>", "", text)
        text = re.sub(r"[^a-zA-Z\s]", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        words = text.split()
        words = [
            self.lemmatizer.lemmatize(w)
            for w in words
            if w not in self.stop_words
        ]
        return " ".join(words)

    def initiate_data_transformation(self):
        try:
            logger.info("Data transformation started")

            df = pd.read_csv(self.config.data_path)
            logger.info(f"Loaded data with shape: {df.shape}")

            # Drop serial number column
            if "Unnamed: 0" in df.columns:
                df.drop(columns=["Unnamed: 0"], inplace=True)

            # Handle missing values
            df["title"] = df["title"].fillna("")
            df["text"] = df["text"].fillna("")
            df = df[~((df["title"] == "") & (df["text"] == ""))]
            logger.info(f"Shape after dropping empty rows: {df.shape}")

            # Combine title + text
            df["content"] = (df["title"] + " " + df["text"]).str.strip()

            # Clean text
            logger.info("Cleaning text...")
            df["content"] = df["content"].apply(self.clean_text)

            # Drop empty rows after cleaning
            df = df[df["content"] != ""]
            logger.info(f"Shape after cleaning: {df.shape}")

            # Train-test split
            X = df["content"]
            y = df["label"]

            X_train, X_test, y_train, y_test = train_test_split(
                X,
                y,
                test_size=self.params["test_size"],
                random_state=self.params["random_state"],
                stratify=y,
            )

            # Save train and test sets
            train_df = pd.DataFrame({"content": X_train, "label": y_train})
            test_df = pd.DataFrame({"content": X_test, "label": y_test})

            os.makedirs(
                os.path.dirname(self.config.transformed_train_path),
                exist_ok=True,
            )
            train_df.to_csv(self.config.transformed_train_path, index=False)
            test_df.to_csv(self.config.transformed_test_path, index=False)

            logger.info(f"Train set: {train_df.shape}")
            logger.info(f"Test set: {test_df.shape}")
            logger.info("Data transformation completed")

        except Exception as e:
            raise CustomException(e, sys)
