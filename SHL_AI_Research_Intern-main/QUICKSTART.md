# Quick Start Guide

Get the SHL Assessment Recommendation System up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (free tier available at https://ai.google.dev/)

## Setup Steps

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Create Sample Data

```bash
python create_sample_data.py
```

This creates `data/assessments.json` with sample SHL assessments.

### 4. Start the API Server

```bash
python run_server.py
```

The API will be available at `http://localhost:8000`

### 5. Test the API

Open a new terminal and run:
```bash
python test_api.py
```

### 6. Use the Frontend

Open `frontend/index.html` in your web browser, or:
```bash
cd frontend
python -m http.server 8080
```
Then visit `http://localhost:8080`

## API Usage Examples

### Health Check
```bash
curl http://localhost:8000/health
```

### Get Recommendations
```bash
curl -X POST http://localhost:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "I am hiring for Java developers who can collaborate with teams"}'
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/recommend",
    json={"query": "Java developer with good communication skills"}
)

print(response.json())
```

## Generate Predictions for Test Set

1. Place your test set in `data/test.csv` with a column named `query`
2. Run:
```bash
python evaluation.py
```
3. Predictions will be saved to `predictions.csv`

## Project Structure

```
.
├── main.py              # FastAPI application
├── recommender.py       # Recommendation engine
├── scraper.py           # Web scraper (optional)
├── evaluation.py        # Generate predictions
├── frontend/
│   └── index.html       # Web interface
├── data/
│   └── assessments.json # Assessment data
└── requirements.txt     # Dependencies
```

## Next Steps

- Deploy to cloud (see DEPLOYMENT.md)
- Customize recommendations (modify `recommender.py`)
- Add more assessments (run `scraper.py` or update `data/assessments.json`)

## Troubleshooting

**Issue:** "GEMINI_API_KEY not found"
- Solution: Create `.env` file with your API key

**Issue:** "No assessments found"
- Solution: Run `python create_sample_data.py`

**Issue:** API not responding
- Solution: Check if server is running on correct port

**Issue:** Frontend can't connect to API
- Solution: Update API URL in `frontend/index.html` to match your server URL

