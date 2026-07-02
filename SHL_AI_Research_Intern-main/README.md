# SHL Assessment Recommendation System


An intelligent recommendation system that helps hiring managers and recruiters find the right SHL assessments for their roles using natural language queries or job descriptions.

## Features

- Natural language query processing
- Job description text/URL support
- Recommends 5-10 most relevant SHL assessments
- Balanced recommendations across multiple domains (technical + behavioral)
- RESTful API with JSON responses
- Web-based frontend for easy testing

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables (create `.env` file):
```
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional, for embeddings
```

3. Run the scraper to collect assessment data:
```bash
python scraper.py
```

4. Start the API server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

5. Open the frontend:
- Navigate to `frontend/index.html` in your browser, or
- Access via the API base URL

## API Endpoints

### Health Check
- `GET /health` - Returns API status

### Recommendations
- `POST /recommend` - Get assessment recommendations
  - Body: `{"query": "your query here"}` or `{"url": "job description URL"}`

## Project Structure

```
.
├── main.py                 # FastAPI application
├── scraper.py             # Web scraper for SHL catalog
├── recommender.py         # Recommendation engine
├── data/
│   ├── assessments.json   # Scraped assessment data
│   ├── train.csv          # Labeled training set
│   └── test.csv           # Unlabeled test set
├── frontend/
│   └── index.html         # Web frontend
├── evaluation.py          # Evaluation script
└── requirements.txt       # Python dependencies

```

