"""
Vercel serverless function with Mangum adapter
"""

import sys
import os

# Add to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import FastAPI app
from app.main import app

# Mangum adapter for AWS Lambda/Vercel
from mangum import Mangum

handler = Mangum(app, lifespan="off")
