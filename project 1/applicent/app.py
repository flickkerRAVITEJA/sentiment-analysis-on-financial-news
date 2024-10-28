from fastapi import FastAPI, Request
from transformers import pipeline

app = FastAPI()
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

@app.post("/predict")
async def predict_sentiment(request: Request):
    data = await request.json()
    text = data["text"]
    result = sentiment_analyzer(text)
    return {"sentiment": result[0]["label"], "score": result[0]["score"]}

# To run: uvicorn app:app --reload --port 8000
