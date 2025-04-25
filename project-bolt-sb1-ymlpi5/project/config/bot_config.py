"""
Configuration settings for the Tennis Under Bot.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("Telegram token not found in environment variables")

# API Settings
REQUEST_TIMEOUT = 10  # seconds
MAX_RETRIES = 3

# Tennis data configuration
SURFACES = ['clay', 'hard', 'grass']
MIN_GAMES_HISTORY = 5  # Minimum number of recent games to analyze
CONFIDENCE_THRESHOLD = 70  # Minimum confidence percentage for recommendations