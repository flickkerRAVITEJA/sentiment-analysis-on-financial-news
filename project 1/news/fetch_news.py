import requests

def fetch_news(api_key, query="market"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    for article in articles[:5]:  # Display first 5 articles for now
        print(article["title"], "-", article["description"])

api_key = "126edad424c94343934ec97683d36a45"  # Replace with your API key
fetch_news(api_key)
