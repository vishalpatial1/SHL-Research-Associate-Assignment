# Deployment Guide

This guide explains how to deploy the SHL Assessment Recommendation System to various cloud platforms.

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

3. **Create sample data:**
   ```bash
   python create_sample_data.py
   ```

4. **Run the API server:**
   ```bash
   python run_server.py
   # Or: uvicorn main:app --reload
   ```

5. **Test the API:**
   ```bash
   python test_api.py
   ```

6. **Open the frontend:**
   - Open `frontend/index.html` in your browser
   - Or serve it using a simple HTTP server:
     ```bash
     cd frontend
     python -m http.server 8080
     ```

## Cloud Deployment Options

### Option 1: Render.com (Recommended - Free Tier)

1. **Create a new Web Service on Render**
2. **Connect your GitHub repository**
3. **Configure:**
   - **Build Command:** `pip install -r requirements.txt && python create_sample_data.py`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables:**
     - `GEMINI_API_KEY`: Your Gemini API key
     - `PORT`: 10000 (or leave empty, Render sets it automatically)

4. **Deploy**

### Option 2: Railway.app

1. **Create a new project on Railway**
2. **Connect GitHub repository**
3. **Add environment variables:**
   - `GEMINI_API_KEY`
4. **Railway will auto-detect Python and install dependencies**
5. **Add a start command in `Procfile`:**
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

### Option 3: Heroku

1. **Create `Procfile`:**
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

2. **Create `runtime.txt`:**
   ```
   python-3.11.0
   ```

3. **Deploy:**
   ```bash
   heroku create your-app-name
   heroku config:set GEMINI_API_KEY=your_key
   git push heroku main
   ```

### Option 4: Google Cloud Run

1. **Create `Dockerfile`:**
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   RUN python create_sample_data.py
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
   ```

2. **Deploy:**
   ```bash
   gcloud run deploy shl-recommender --source .
   ```

### Option 5: AWS Lambda (with API Gateway)

Use a framework like Mangum to wrap FastAPI:
```python
from mangum import Mangum
handler = Mangum(app)
```

## Frontend Deployment

### Option 1: GitHub Pages

1. **Move frontend files to `docs/` folder**
2. **Update API URL in `index.html` to your deployed API URL**
3. **Enable GitHub Pages in repository settings**

### Option 2: Netlify/Vercel

1. **Create a new site**
2. **Connect repository**
3. **Set build directory to `frontend/`**
4. **Update API URL in `index.html`**

### Option 3: Static Hosting

Upload `frontend/index.html` to any static hosting service and update the API URL.

## Environment Variables

Required:
- `GEMINI_API_KEY`: Google Gemini API key (get from https://ai.google.dev/)

Optional:
- `PORT`: Server port (default: 8000)
- `OPENAI_API_KEY`: Alternative API key (not required)

## Testing Deployment

After deployment, test your API:

1. **Health Check:**
   ```bash
   curl https://your-api-url.com/health
   ```

2. **Recommendation:**
   ```bash
   curl -X POST https://your-api-url.com/recommend \
     -H "Content-Type: application/json" \
     -d '{"query": "Java developer"}'
   ```

## Troubleshooting

- **API not responding:** Check environment variables and logs
- **Embeddings not loading:** Ensure `data/assessments.json` exists
- **LLM errors:** Verify `GEMINI_API_KEY` is set correctly
- **CORS errors:** Update CORS settings in `main.py` if needed

