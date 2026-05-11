import sys
from pathlib import Path

# Add the english-to-kannada directory to the path
sys.path.insert(0, str(Path(__file__).parent.parent / 'english-to-kannada'))

from app import app

# Export the Flask app for Vercel
__all__ = ['app']
