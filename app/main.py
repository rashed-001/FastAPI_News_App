from fastapi import FastAPI
from .database import engine, get_db
from .models import Base
from .routes import news

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the news router
app.include_router(news.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the News API!"}