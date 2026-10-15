"""Point d'entrée Vercel : expose l'application FastAPI du Dashboard Nexbot."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexbot.dashboard.app import app  # noqa: E402,F401
