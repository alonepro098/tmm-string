import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "frozentools").strip()

if not API_ID:
    print("WARNING: No API_ID found in environment variables.")
if not API_HASH:
    print("WARNING: No API_HASH found in environment variables.")
if not BOT_TOKEN:
    print("WARNING: No BOT_TOKEN found in environment variables.")

try:
    if API_ID:
        API_ID = int(API_ID)
except ValueError:
    print("ERROR: API_ID must be a valid integer.")

if DATABASE_URL and "postgres://" in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
