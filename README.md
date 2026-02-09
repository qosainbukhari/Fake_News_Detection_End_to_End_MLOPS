# Fake News Detection

An end-to-end machine learning project that classifies news articles as **Real** or **Fake** using NLP and a modular pipeline architecture.

## Dataset

**WELFake Dataset** — 72,134 news articles (35,028 real + 37,106 fake) merged from four sources (Kaggle, McIntire, Reuters, BuzzFeed Political).

- **Source:** [Kaggle - Fake News Classification](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)
- **Columns:** `title`, `text`, `label` (0 = Fake, 1 = Real)
- **License:** CC BY 4.0

## Model Performance

| Metric | Score |
|---|---|
| Accuracy | 95.63% |
| Precision | 94.76% |
| Recall | 96.86% |
| F1-Score | 95.80% |

### Models Compared

| Model | F1-Score |
|---|---|
| **Random Forest** | **95.80%** |
| Logistic Regression | 95.07% |
| Gradient Boosting | 94.45% |
| Decision Tree | 93.53% |

## Tech Stack

- **Language:** Python 3.10
- **ML:** scikit-learn, NLTK
- **API:** FastAPI, Uvicorn
- **Tracking:** MLflow
- **Pipeline:** DVC
- **Containerization:** Docker

## Project Structure

```
fake-news-detection/
├── app.py                         # FastAPI application
├── main.py                        # Full pipeline runner
├── setup.py                       # Package installer
├── params.yaml                    # Model hyperparameters
├── dvc.yaml                       # DVC pipeline stages
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
│
├── config/
│   └── config.yaml                # Pipeline paths & MLflow config
│
├── src/
│   ├── logger.py                  # Logging setup
│   ├── exception.py               # Custom exception handler
│   ├── constant/                  # File path constants
│   ├── entity/                    # Dataclass configurations
│   ├── utils/                     # Helper functions
│   ├── configuration/             # Configuration manager
│   ├── components/
│   │   ├── data_ingestion.py      # Read raw data
│   │   ├── data_transformation.py # Clean text, train-test split
│   │   ├── model_trainer.py       # TF-IDF + Random Forest training
│   │   └── model_evaluation.py    # Metrics + MLflow tracking
│   └── pipeline/
│       ├── data_ingestion_pipeline.py
│       ├── data_transformation_pipeline.py
│       ├── model_trainer_pipeline.py
│       ├── model_evaluation_pipeline.py
│       └── prediction_pipeline.py
│
├── notebooks/
│   ├── 01_EDA.ipynb               # Exploratory data analysis
│   ├── 02_data_preprocessing.ipynb # Text cleaning experiments
│   └── 03_model_training.ipynb    # Model comparison
│
├── templates/
│   └── index.html                 # Frontend UI
├── static/
│   ├── style.css                  # Dark theme styling
│   └── script.js                  # API fetch logic
│
├── data/
│   └── raw/                       # Raw dataset (WELFake_Dataset.csv)
└── artifacts/                     # Generated pipeline outputs
    ├── data_ingestion/
    ├── data_transformation/
    ├── model_trainer/
    └── model_evaluation/
```

## Pipeline Architecture

```
Data Ingestion → Data Transformation → Model Training → Model Evaluation
                                                              ↓
                                                        MLflow Tracking
```

**Data Ingestion** — Reads raw CSV from `data/raw/`, copies to artifacts.

**Data Transformation** — Drops nulls, combines title + text, cleans text (lowercase, remove URLs/HTML/special chars, remove stopwords, lemmatize), splits 80/20 stratified.

**Model Training** — TF-IDF vectorization (5000 features) + Random Forest classifier. Saves model and vectorizer.

**Model Evaluation** — Computes accuracy, precision, recall, F1-score. Logs everything to MLflow.

## Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/fake-news-detection.git
cd fake-news-detection
```

### 2. Create conda environment

```bash
conda create -n fakenews python=3.10 -y
conda activate fakenews
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

### 4. Download dataset

Download the [WELFake Dataset](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification) and place the CSV at:

```
data/raw/WELFake_Dataset.csv
```

## Usage

### Run full pipeline

```bash
python main.py
```

### Run with DVC

```bash
dvc repro
dvc metrics show
```

### Start MLflow UI

```bash
mlflow ui
```

Open http://localhost:5000 to view experiment tracking.

### Start FastAPI app

```bash
uvicorn app:app --reload
```

Open http://localhost:8000 for the web UI.

### Docker

```bash
docker-compose up --build
```

Open http://localhost:8000.

## API Reference

### `POST /predict`

**Request:**

```json
{
  "text": "Breaking news article text here..."
}
```

**Response:**

```json
{
  "prediction": "Real News"
}
```

## Notebooks

| Notebook | Description |
|---|---|
| `01_EDA.ipynb` | Dataset exploration, missing values, label distribution, text length analysis |
| `02_data_preprocessing.ipynb` | Text cleaning, stopword removal, lemmatization, train-test split |
| `03_model_training.ipynb` | TF-IDF + 4 model comparison, confusion matrix, best model selection |

## License

This project uses the [WELFake Dataset](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification) licensed under CC BY 4.0.
