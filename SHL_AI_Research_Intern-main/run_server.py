"""
Convenience script to run the API server
"""

import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    print(f"Starting SHL Assessment Recommendation API on port {port}")
    print(f"API Documentation: http://localhost:{port}/docs")
    print(f"Health Check: http://localhost:{port}/health")
    print(f"\nPress Ctrl+C to stop the server")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )

