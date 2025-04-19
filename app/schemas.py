from pydantic import BaseModel, HttpUrl
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    description: str | None = None
    url: HttpUrl
    published_at: datetime
    source: str | None = None
    country: str | None = None

class NewsCreate(NewsBase):
    pass

class NewsResponse(NewsBase):
    id: int

    class Config:
        orm_mode = True