from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import News
from ..schemas import NewsCreate, NewsResponse
from ..utils import fetch_news_from_api

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/", response_model=list[NewsResponse])
def get_all_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    news = db.query(News).offset(skip).limit(limit).all()
    return news

@router.post("/save-latest", response_model=list[NewsResponse])
def save_latest_news(db: Session = Depends(get_db)):
    latest_news = fetch_news_from_api()
    if not latest_news:
        raise HTTPException(status_code=400, detail="Failed to fetch news")
    
    saved_news = []
    for article in latest_news[:3]:  # Save top 3 articles
        news_item = News(**article)
        db.add(news_item)
        saved_news.append(news_item)
    db.commit()
    return saved_news

@router.get("/headlines/country/{country_code}", response_model=list[NewsResponse])
def get_headlines_by_country(country_code: str, db: Session = Depends(get_db)):
    return fetch_news_from_api(country=country_code)

@router.get("/headlines/source/{source_id}", response_model=list[NewsResponse])
def get_headlines_by_source(source_id: str, db: Session = Depends(get_db)):
    return fetch_news_from_api(source=source_id)

@router.get("/headlines/filter", response_model=list[NewsResponse])
def get_headlines_by_filter(country: str = None, source: str = None, db: Session = Depends(get_db)):
    return fetch_news_from_api(country=country, source=source)