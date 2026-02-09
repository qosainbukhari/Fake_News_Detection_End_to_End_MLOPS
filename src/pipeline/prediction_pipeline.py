import re
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.logger import logger

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load("artifacts/model_trainer/model.joblib")
        self.tfidf = joblib.load(
            "artifacts/model_trainer/tfidf_vectorizer.joblib"
        )
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

    def predict(self, text: str) -> str:
        cleaned = self.clean_text(text)
        vectorized = self.tfidf.transform([cleaned])
        prediction = self.model.predict(vectorized)[0]
        result = "Real News" if prediction == 1 else "Fake News"
        logger.info(f"Prediction: {result}")
        return result
