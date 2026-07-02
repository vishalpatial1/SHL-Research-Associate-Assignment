# 🚀 Quick Start Guide - SHL Assessment Recommendation System

## ✅ Project is Running!

The API server is starting up. Here's how to use it:

---

## 📍 Access Points

### 1. API Server
- **URL:** http://localhost:8000
- **Status:** Starting up (wait 10-15 seconds)

### 2. API Documentation (Swagger UI)
- **URL:** http://localhost:8000/docs
- **Features:** Interactive API testing interface

### 3. Health Check
- **URL:** http://localhost:8000/health
- **Test:** Open in browser to verify server is running

### 4. Frontend Interface
- **File:** `frontend/index.html`
- **Open:** Double-click the file or use a web server

---

## 🧪 Test the API

### Method 1: Browser (Easiest)

1. **Open API Documentation:**
   - Go to: http://localhost:8000/docs
   - This opens FastAPI's interactive Swagger UI

2. **Test Health Endpoint:**
   - Click on `GET /health`
   - Click "Try it out"
   - Click "Execute"
   - See the response

3. **Test Recommendations:**
   - Click on `POST /recommend`
   - Click "Try it out"
   - Enter in Request body:
     ```json
     {
       "query": "I am hiring for Java developers who can collaborate with teams"
     }
     ```
   - Click "Execute"
   - See the recommendations!

### Method 2: Using Frontend

1. **Open Frontend:**
   - Navigate to: `frontend/index.html`
   - Double-click to open in browser

2. **Enter Query:**
   - Type: "I am hiring for Java developers who can collaborate with teams"
   - Click "Get Recommendations"

3. **View Results:**
   - See the recommended assessments in a beautiful table format!

### Method 3: Using Python

```python
import requests

# Test health
response = requests.get("http://localhost:8000/health")
print("Health:", response.json())

# Get recommendations
response = requests.post(
    "http://localhost:8000/recommend",
    json={"query": "Java developer with good communication skills"}
)
data = response.json()
print(f"\nFound {data['count']} recommendations:")
for rec in data['recommendations']:
    print(f"- {rec['name']}: {rec['url']}")
```

### Method 4: Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Get recommendations
curl -X POST http://localhost:8000/recommend ^
  -H "Content-Type: application/json" ^
  -d "{\"query\": \"Java developer with good communication skills\"}"
```

---

## 📋 Sample Queries to Test

1. **Technical + Behavioral:**
   ```
   I am hiring for Java developers who can also collaborate effectively with my business teams.
   ```

2. **Multiple Skills:**
   ```
   Looking to hire mid-level professionals who are proficient in Python, SQL and Java Script.
   ```

3. **Analyst Role:**
   ```
   I am hiring for an analyst and wants applications to screen using Cognitive and personality tests
   ```

---

## 🎯 What You'll See

### API Response Example:
```json
{
  "recommendations": [
    {
      "name": "Verify Java",
      "url": "https://www.shl.com/solutions/products/verify-java/",
      "description": "Java programming assessment...",
      "test_type": "Knowledge & Skills"
    },
    {
      "name": "OPQ32",
      "url": "https://www.shl.com/solutions/products/opq32/",
      "description": "Personality assessment...",
      "test_type": "Personality & Behavior"
    }
    // ... 3-8 more recommendations
  ],
  "query": "Your query text",
  "count": 10
}
```

---

## ⚙️ Server Management

### Stop the Server
- Press `Ctrl+C` in the terminal where the server is running

### Restart the Server
```bash
python run_server.py
```

### Change Port
- Edit `.env` file: `PORT=8080`
- Or edit `run_server.py`

---

## 🐛 Troubleshooting

### Server not responding?
1. Wait 10-15 seconds for startup
2. Check terminal for error messages
3. Verify port 8000 is not in use:
   ```powershell
   netstat -ano | findstr :8000
   ```

### "Module not found" error?
```bash
pip install -r requirements.txt
```

### Frontend can't connect?
- Make sure API server is running
- Check API URL in `frontend/index.html` is `http://localhost:8000`

---

## ✅ Verification Checklist

- [ ] Server is running (check http://localhost:8000/health)
- [ ] API docs accessible (http://localhost:8000/docs)
- [ ] Can get recommendations via API
- [ ] Frontend can connect to API
- [ ] Recommendations are relevant and balanced

---

## 🎉 You're All Set!

The project is running and ready to use. Try the different methods above to test the recommendation system!

**Next Steps:**
1. Test with sample queries
2. Try the frontend interface
3. Generate predictions: `python evaluation.py`

---

**Server URL:** http://localhost:8000  
**API Docs:** http://localhost:8000/docs  
**Frontend:** `frontend/index.html`

