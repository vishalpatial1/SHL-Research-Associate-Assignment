# How to Run the SHL Assessment Recommendation System

## ✅ Server Status

The API server is starting up! Here's how to use it:

---

## 🚀 Quick Start

### 1. API Server
The server is running at: **http://localhost:8000**

### 2. Test the API

#### Health Check
Open in browser or use curl:
```
http://localhost:8000/health
```

#### Get Recommendations
```bash
curl -X POST http://localhost:8000/recommend \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"I am hiring for Java developers who can collaborate with teams\"}"
```

### 3. Use the Frontend

1. **Open the frontend:**
   - Navigate to: `frontend/index.html`
   - Double-click to open in your browser

2. **Or use Python HTTP server:**
   ```bash
   cd frontend
   python -m http.server 8080
   ```
   Then open: http://localhost:8080

3. **Test with sample queries:**
   - "I am hiring for Java developers who can also collaborate effectively with my business teams."
   - "Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script."

---

## 📋 API Endpoints

### Health Check
- **URL:** `GET http://localhost:8000/health`
- **Response:**
  ```json
  {
    "status": "healthy",
    "service": "SHL Assessment Recommendation API",
    "version": "1.0.0"
  }
  ```

### Get Recommendations
- **URL:** `POST http://localhost:8000/recommend`
- **Request Body:**
  ```json
  {
    "query": "Your query here"
  }
  ```
  OR
  ```json
  {
    "url": "https://example.com/job-description"
  }
  ```
- **Response:**
  ```json
  {
    "recommendations": [
      {
        "name": "Assessment Name",
        "url": "https://www.shl.com/...",
        "description": "...",
        "test_type": "Knowledge & Skills"
      }
    ],
    "query": "Your query",
    "count": 10
  }
  ```

---

## 🧪 Test the API

### Using Python
```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Get recommendations
response = requests.post(
    "http://localhost:8000/recommend",
    json={"query": "Java developer with good communication skills"}
)
print(response.json())
```

### Using Browser
1. Open: http://localhost:8000/docs
2. This opens FastAPI's interactive documentation (Swagger UI)
3. You can test endpoints directly from the browser

---

## 🛠️ Troubleshooting

### Server not starting?
1. Check if port 8000 is available:
   ```bash
   netstat -ano | findstr :8000
   ```
2. Change port in `run_server.py` or `.env` file

### API not responding?
1. Check server logs in the terminal
2. Verify `.env` file has `GEMINI_API_KEY` set
3. Ensure `data/assessments.json` exists

### Frontend not connecting?
1. Update API URL in `frontend/index.html`:
   ```javascript
   const API_BASE_URL = 'http://localhost:8000';
   ```
2. Make sure API server is running

---

## 📊 Current Status

- ✅ Python 3.13.7 installed
- ✅ FastAPI installed
- ✅ Assessment data ready
- ✅ Server starting on port 8000

---

## 🎯 Next Steps

1. **Test Health Endpoint:**
   - Open: http://localhost:8000/health

2. **Test Recommendations:**
   - Open: http://localhost:8000/docs
   - Use the interactive API documentation

3. **Use Frontend:**
   - Open `frontend/index.html` in browser
   - Enter a query and get recommendations

4. **Generate Predictions:**
   ```bash
   python evaluation.py
   ```

---

## 📝 Notes

- The server runs on **port 8000** by default
- API documentation available at: **http://localhost:8000/docs**
- Frontend can be opened directly or served via HTTP server
- All endpoints return JSON format

---

**Server is running!** 🎉

