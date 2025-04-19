import requests
from fastapi import HTTPException
from datetime import datetime

NEWS_API_KEY = "your_newsapi_key_here"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news_from_api(country: str = None, source: str = None):
    params = {"apiKey": NEWS_API_KEY}
    if country:
        params["country"] = country
    if source:
        params["sources"] = source

    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch news")
    
    articles = response.json().get("articles", [])
    formatted_articles = []
    for article in articles:
        formatted_articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "published_at": datetime.strptime(article.get("publishedAt"), "%Y-%m-%dT%H:%M:%SZ"),
            "source": article.get("source", {}).get("name"),
            "country": country,
        })
    return formatted_articles