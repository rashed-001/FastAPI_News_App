import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Set up a test database (SQLite in-memory)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the test database
Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture
def setup_test_data():
    """Fixture to set up initial test data."""
    db = TestingSessionLocal()
    db.execute("DELETE FROM news")  # Clear the table before each test
    db.commit()
    db.close()

def test_get_all_news(setup_test_data):
    response = client.get("/news/")
    assert response.status_code == 200
    assert response.json() == []

def test_save_latest_news(setup_test_data, mocker):
    # Mock the fetch_news_from_api function
    mocker.patch("app.utils.fetch_news_from_api", return_value=[
        {
            "title": "Test News 1",
            "description": "Description 1",
            "url": "http://example.com/1",
            "published_at": "2025-04-20T12:00:00Z",
            "source": "Source 1",
            "country": "us",
        },
        {
            "title": "Test News 2",
            "description": "Description 2",
            "url": "http://example.com/2",
            "published_at": "2025-04-20T13:00:00Z",
            "source": "Source 2",
            "country": "us",
        },
    ])
    response = client.post("/news/save-latest")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Test News 1"
    assert data[1]["title"] == "Test News 2"

def test_get_headlines_by_country(setup_test_data, mocker):
    # Mock the fetch_news_from_api function
    mocker.patch("app.utils.fetch_news_from_api", return_value=[
        {
            "title": "Country News",
            "description": "Description",
            "url": "http://example.com/country",
            "published_at": "2025-04-20T14:00:00Z",
            "source": "Source",
            "country": "us",
        }
    ])
    response = client.get("/news/headlines/country/us")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["country"] == "us"

def test_get_headlines_by_source(setup_test_data, mocker):
    # Mock the fetch_news_from_api function
    mocker.patch("app.utils.fetch_news_from_api", return_value=[
        {
            "title": "Source News",
            "description": "Description",
            "url": "http://example.com/source",
            "published_at": "2025-04-20T15:00:00Z",
            "source": "source_id",
            "country": "us",
        }
    ])
    response = client.get("/news/headlines/source/source_id")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["source"] == "source_id"

def test_get_headlines_by_filter(setup_test_data, mocker):
    # Mock the fetch_news_from_api function
    mocker.patch("app.utils.fetch_news_from_api", return_value=[
        {
            "title": "Filtered News",
            "description": "Description",
            "url": "http://example.com/filter",
            "published_at": "2025-04-20T16:00:00Z",
            "source": "source_id",
            "country": "us",
        }
    ])
    response = client.get("/news/headlines/filter?country=us&source=source_id")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["country"] == "us"
    assert data[0]["source"] == "source_id"