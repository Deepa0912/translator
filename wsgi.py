import sys
from pathlib import Path

# Add the english-to-kannada directory to Python path
sys.path.insert(0, str(Path(__file__).parent / 'english-to-kannada'))

from app import app

if __name__ == "__main__":
    app.run()
