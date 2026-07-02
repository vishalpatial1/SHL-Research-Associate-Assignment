# 🚀 Run Commands - SHL Assessment Recommendation System

## Quick Start Commands

### 1. Start the API Server

**Main Command:**
```bash
python run_server.py
```

**Alternative:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**What it does:**
- Starts the FastAPI server on port 8000
- API will be available at: `http://localhost:8000`
- Auto-reloads on code changes

---

### 2. Test the API

**Using Python:**
```bash
python test_api.py
```

**Using cURL:**
```bash
# Health check
curl http://localhost:8000/health

# Get recommendations
curl -X POST http://localhost:8000/recommend -H "Content-Type: application/json" -d "{\"query\": \"Java developer\"}"
```

---

### 3. Generate Predictions

**Generate predictions CSV:**
```bash
python evaluation.py
```

**This creates:**
- `predictions.csv` - Default output
- `jay_tiwari.csv` - Submission file (copy of predictions.csv)

---

### 4. Setup Commands

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Create sample data:**
```bash
python create_sample_data.py
```

**Setup API key:**
```bash
python setup_api_key.py
```

**Setup dataset:**
```bash
python setup_dataset.py
```

---

## Complete Workflow

### First Time Setup:
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create sample assessment data
python create_sample_data.py

# 3. Setup API key (already done)
# API key is in .env file

# 4. Start the server
python run_server.py
```

### Daily Usage:
```bash
# Start server
python run_server.py

# In another terminal, test it
python test_api.py

# Or open in browser
# http://localhost:8000/docs
```

### Generate Predictions:
```bash
# Make sure test.csv is in data/ directory
python evaluation.py

# This creates jay_tiwari.csv for submission
```

---

## Server URLs

Once the server is running:

- **API Base:** http://localhost:8000
- **Health Check:** http://localhost:8000/health
- **API Documentation:** http://localhost:8000/docs
- **Recommendations:** http://localhost:8000/recommend (POST)

---

## Frontend

**Option 1: Direct Open**
- Navigate to: `frontend/index.html`
- Double-click to open in browser

**Option 2: HTTP Server**
```bash
cd frontend
python -m http.server 8080
```
Then open: http://localhost:8080

---

## Stop Server

Press `Ctrl+C` in the terminal where the server is running.

---

## Troubleshooting

### Port Already in Use?
```bash
# Change port in .env file
PORT=8080

# Or in run_server.py
port = 8000  # Change to 8080
```

### Module Not Found?
```bash
pip install -r requirements.txt
```

### Server Not Starting?
```bash
# Check if port is available
netstat -ano | findstr :8000

# Check Python version
python --version  # Should be 3.8+
```

---

## Summary

**Most Common Commands:**

1. **Start Server:**
   ```bash
   python run_server.py
   ```

2. **Test API:**
   ```bash
   python test_api.py
   ```

3. **Generate Predictions:**
   ```bash
   python evaluation.py
   ```

4. **Open API Docs:**
   - Browser: http://localhost:8000/docs

---

**That's it!** 🎉

