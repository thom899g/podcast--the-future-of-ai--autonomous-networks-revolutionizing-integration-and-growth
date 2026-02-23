"""
Configuration module for podcast generation system.
Centralizes environment variables, constants, and Firebase configuration.
"""
import os
import sys
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Firebase configuration
FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH', './firebase-credentials.json')
FIRESTORE_COLLECTION = "podcast_episodes"

# Episode configuration
EPISODE_CONFIG = {
    "number": 50,
    "title": "The Future of AI: Autonomous Networks Revolutionizing Integration and Growth",
    "hook": "Dive into the latest advancements in autonomous networks and how they are reshaping integration and growth across industries.",
    "tags": ["AI", "Autonomous Networks", "Integration Growth", "Neural Networks"],
    "target_duration_minutes": 45
}

# Social media configuration
TWITTER_HANDLE = "@EvolutionEcoSys"
MAX_TWEET_LENGTH = 280

def validate_config() -> bool:
    """Validate critical configuration before execution."""
    if not os.path.exists(FIREBASE_CREDENTIALS_PATH):
        print(f"ERROR: Firebase credentials not found at {FIREBASE_CREDENTIALS_PATH}")
        return False
    
    required_env_vars = ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_CHAT_ID']
    for var in required_env_vars:
        if not os.getenv(var):
            print(f"ERROR: {var} not set in environment")
            return False
    
    return True