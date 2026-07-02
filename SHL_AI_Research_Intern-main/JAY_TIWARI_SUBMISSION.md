# SHL Assessment Recommendation System
## Submission by Jay Tiwari - AI Reach Intern

---

## Candidate Information

- **Name:** Jay Tiwari
- **Position:** AI Reach Intern
- **Company:** SHL Company
- **Project:** SHL Assessment Recommendation System

---

## Submission Status: ✅ READY

All code, documentation, and configuration are complete and ready for deployment.

---

## Configuration

### API Key
- **Gemini API Key:** Configured in `.env` file
- **Status:** API key is set up (system works with or without LLM)

### Project Files
All required files are present and functional:
- ✅ FastAPI backend (`main.py`)
- ✅ Recommendation engine (`recommender.py`)
- ✅ Web scraper (`scraper.py`)
- ✅ Frontend (`frontend/index.html`)
- ✅ Evaluation script (`evaluation.py`)
- ✅ Approach document (`APPROACH.md`)
- ✅ Assessment data (`data/assessments.json`)

---

## Submission Requirements

### 1. Three URLs (To be provided after deployment)

#### A. API Endpoint URL
- **Status:** ⚠️ Needs deployment
- **Instructions:** Deploy to Render.com, Railway.app, or similar
- **Endpoints:**
  - `GET /health` - Health check
  - `POST /recommend` - Get recommendations

#### B. GitHub Repository URL
- **Status:** ⚠️ Needs to be created
- **Instructions:** 
  1. Create GitHub repository
  2. Push all code
  3. Make accessible (public or shared private)

#### C. Web Application Frontend URL
- **Status:** ⚠️ Needs deployment
- **Instructions:** Deploy `frontend/index.html` to GitHub Pages/Netlify
- **Note:** Update API URL in frontend after API deployment

### 2. Approach Document
- **File:** `APPROACH.md`
- **Status:** ✅ Complete (2 pages)
- **Content:** Methodology, optimization journey, technology stack

### 3. Predictions CSV
- **File:** `predictions.csv` (to be generated)
- **Status:** ⚠️ Needs actual test set
- **Format:** `Query,Assessment_url` (multiple rows per query)
- **Generate:** Run `python evaluation.py` after adding actual test.csv

---

## Quick Start

### 1. Test Locally
```bash
# Start API server
python run_server.py

# Test API (in another terminal)
python test_api.py

# Generate predictions (when test.csv is ready)
python evaluation.py
```

### 2. Deploy
Follow instructions in `DEPLOYMENT.md`:
- Deploy API to cloud platform
- Deploy frontend to static hosting
- Push code to GitHub

---

## Key Features

1. **Intelligent Recommendations**
   - Semantic search with embeddings
   - LLM-based reranking (Gemini Pro)
   - Domain balancing (technical + behavioral)

2. **Multi-Input Support**
   - Natural language queries
   - Job description text
   - Job description URLs

3. **Production Ready**
   - Error handling
   - API documentation
   - Comprehensive testing

---

## Project Structure

```
.
├── main.py                 # FastAPI backend
├── recommender.py         # Recommendation engine
├── scraper.py             # Web scraper
├── evaluation.py          # Generate predictions
├── frontend/
│   └── index.html         # Web interface
├── data/
│   ├── assessments.json  # 30 assessments
│   ├── train.csv         # Training set
│   └── test.csv            # Test set (needs actual data)
├── APPROACH.md            # 2-page approach document
└── requirements.txt      # Dependencies
```

---

## Notes

- API key is configured in `.env` file
- System works with or without LLM (graceful fallback)
- All code is production-ready
- Documentation is complete

---

## Contact

**Jay Tiwari**  
AI Reach Intern Candidate  
SHL Company

---

**Submission Date:** 2025

