"""
Vercel serverless function entry point
"""

from app.main import app

# Vercel expects the app to be exported
handler = app
