from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from src.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI(title="Fake News Detection API")

app.mount("/static", StaticFiles(directory="static"), name="static")

pipeline = PredictionPipeline()


class NewsInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r") as f:
        return f.read()


@app.post("/predict")
async def predict(news: NewsInput):
    result = pipeline.predict(news.text)
    return {"prediction": result}
