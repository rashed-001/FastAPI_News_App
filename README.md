# FastAPI_News_App for BlockStack


A FastAPI-based backend application that integrates with NewsAPI to fetch and store news articles. The application supports OAuth2 client credentials-based authentication and provides endpoints to fetch, filter, and save news articles.

## Project Structure

```
fastapi-oauth2-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── oauth2.py
│   └── routes
│       ├── __init__.py
│       └── protected.py
├── .flake8
├── .pre-commit-config.yaml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Features

- **OAuth2 Client Credentials Authentication**: Secures endpoints using access tokens.
- **NewsAPI Integration**: Fetches news articles from NewsAPI.
- **Relational Database**: Stores news articles in a relational database (SQLite by default).
- **Dockerized**: Easily deployable using Docker.
- **Unit Tests**: Includes unit tests with at least 80% code coverage.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rashed-001/FastAPI_News_App.git

   cd FastAPI_News_App
   ```

2. **Install Dependencies:**
   -Ensure you have Python 3.12+ installed.
   -Then, install the required dependencies:
  ```bash
      pip install -r requirements.txt
```
3. **Set Up Environment Variables:**
   - Create a .env file in the app directory and add the following:
     ```bash
     NEWS_API_KEY=your_newsapi_key_here
     ```

4. **Run Database Migrations:**
 - The database tables will be created automatically when the application starts.

5. ---

## How to run the server

- **Run Locally: Start the FastAPI server:**: uvicorn app.main:app --reload.
- **Next**: The server will be available at http://127.0.0.1:8000.

- **Access the API Documentation:**: 1. Swagger UI: http://127.0.0.1:8000/docs and 
  2. ReDoc: http://127.0.0.1:8000/redoc
  
---
6. ---

## How to run tests

- **Install Testing Dependencies**: pip install pytest pytest-cov pytest-mock.
- **Run Tests**: pytest --cov=app --cov-report=term-missing

- **Check Coverage **: Ensure the code coverage is at least 80%.
  
---
---

## How to run Docker

- **Build the Docker Image**: docker build -t fastapi-news-app .
- **Run the Docker Container**: docker run -d -p 80:80 fastapi-news-app

- **Access the Application**: Open your browser and navigate to http://localhost.

---

---

##How to Generate Access Tokens and Use Secured Endpoints
- **Generate Access Token**: Use the /token endpoint to generate an access token (if implemented).

- **RUse Secured Endpoints**: Include the token in the <vscode_annotation details='%5B%7B%22title%22%3A%22hardcoded-credentials%22%2C%22description%22%3A%22Embedding%20credentials%20in%20source%20code%20risks%20unauthorized%20access%22%7D%5D'>Authorization</vscode_annotation>`` header:

```bash
curl -H "Authorization: Bearer your_access_token" "http://127.0.0.1:8000/news/"
```

---
---
## App Usage Examples
**1. GET /news**:
-Fetch all news articles with pagination.

-Request:
```bash
curl -X GET "http://127.0.0.1:8000/news/?skip=0&limit=10"
```

-Response:
```bash
[
  {
    "id": 1,
    "title": "News Title",
    "description": "News Description",
    "url": "http://example.com",
    "published_at": "2025-04-20T12:00:00Z",
    "source": "Source Name",
    "country": "us"
  }
]
```

---

---
**2. POST /news/save-latest**
-Fetch the latest news from NewsAPI and save the top 3 articles to the database.

-Request:
```bash
curl -X POST "http://127.0.0.1:8000/news/save-latest"
```

-Response:
```bash
[
  {
    "id": 1,
    "title": "News Title",
    "description": "News Description",
    "url": "http://example.com",
    "published_at": "2025-04-20T12:00:00Z",
    "source": "Source Name",
    "country": "us"
  }
]
```
**3. GET /news/headlines/country/{country_code}**
-Fetch top headlines by country.

Request:
```bash
curl -X GET "http://127.0.0.1:8000/news/headlines/country/us"
```
Response:
```bash
[
  {
    "title": "News Title",
    "description": "News Description",
    "url": "http://example.com",
    "published_at": "2025-04-20T12:00:00Z",
    "source": "Source Name",
    "country": "us"
  }
]
```
**4. GET /news/headlines/source/{source_id}**
-Fetch top headlines by source.

Request:
```bash
curl -X GET "http://127.0.0.1:8000/news/headlines/source/source_id"
```

Response:
```bash
[
  {
    "title": "News Title",
    "description": "News Description",
    "url": "http://example.com",
    "published_at": "2025-04-20T12:00:00Z",
    "source": "source_id",
    "country": "us"
  }
]
```
**5. GET /news/headlines/filter**
-Fetch top headlines by filtering both country and source.

Request: 
```bash
curl -X GET "http://127.0.0.1:8000/news/headlines/filter?country=us&source=source_id"
```

Response:
```bash
[
  {
    "title": "News Title",
    "description": "News Description",
    "url": "http://example.com",
    "published_at": "2025-04-20T12:00:00Z",
    "source": "source_id",
    "country": "us"
  }
]
```
