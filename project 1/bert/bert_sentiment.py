from transformers import pipeline

# Load a pre-trained BERT model for sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Example usage
text = "The company reported great profits this quarter!"
result = sentiment_analyzer(text)
print(result)  # Output: [{'label': '5 stars', 'score': 0.85}]
