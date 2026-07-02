"""
FastAPI Backend for SHL Assessment Recommendation System

Submission by: Jay Tiwari
Position: AI Reach Intern
Company: SHL Company
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict
import uvicorn
from recommender import AssessmentRecommender
import os

app = FastAPI(
    title="SHL Assessment Recommendation API",
    description="API for recommending SHL assessments based on job descriptions or queries",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize recommender (lazy loading)
recommender = None

def get_recommender():
    """Lazy initialization of recommender"""
    global recommender
    if recommender is None:
        recommender = AssessmentRecommender()
    return recommender

class RecommendationRequest(BaseModel):
    query: Optional[str] = None
    url: Optional[str] = None

class AssessmentResponse(BaseModel):
    name: str
    url: str
    description: Optional[str] = None
    test_type: Optional[str] = None

class RecommendationResponse(BaseModel):
    recommendations: List[AssessmentResponse]
    query: str
    count: int

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "SHL Assessment Recommendation API",
        "version": "1.0.0"
    }

@app.post("/recommend", response_model=RecommendationResponse)
async def recommend_assessments(request: RecommendationRequest):
    """
    Get assessment recommendations based on query or URL
    
    - **query**: Natural language query or job description text
    - **url**: URL containing a job description
    """
    try:
        # Get query text
        query_text = None
        
        if request.query:
            query_text = request.query
        elif request.url:
            # Process URL to extract text
            query_text = get_recommender().process_url(request.url)
            if not query_text:
                raise HTTPException(
                    status_code=400,
                    detail="Could not extract text from the provided URL"
                )
        else:
            raise HTTPException(
                status_code=400,
                detail="Either 'query' or 'url' must be provided"
            )
        
        # Get recommendations
        recommendations = get_recommender().recommend(
            query_text,
            min_results=5,
            max_results=10
        )
        
        if not recommendations:
            raise HTTPException(
                status_code=404,
                detail="No recommendations found. Please try a different query."
            )
        
        # Format response
        assessment_responses = [
            AssessmentResponse(
                name=rec['name'],
                url=rec['url'],
                description=rec.get('description', ''),
                test_type=rec.get('test_type', '')
            )
            for rec in recommendations
        ]
        
        return RecommendationResponse(
            recommendations=assessment_responses,
            query=query_text[:200],  # Truncate for display
            count=len(assessment_responses)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "SHL Assessment Recommendation API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "recommend": "/recommend (POST)"
        },
        "docs": "/docs"
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

