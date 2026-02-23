"""
Firebase service module for state management and episode tracking.
Uses Firestore as the primary database for episode metadata and status.
"""
import json
import logging
from typing import Optional, Dict, Any
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.exceptions import FirebaseError

from config import FIREBASE_CREDENTIALS_PATH, FIRESTORE_COLLECTION

# Initialize logger
logger = logging.getLogger(__name__)

class FirebaseService:
    """Manages Firebase Firestore operations for podcast episodes."""
    
    def __init__(self):
        """Initialize Firebase app with error handling."""
        self.db = None
        self._initialize_firebase()
    
    def _initialize_firebase(self) -> None:
        """Initialize Firebase app with credential validation."""
        try:
            # Check if Firebase app already exists
            if not firebase_admin._apps:
                if not FIREBASE_CREDENTIALS_PATH