import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("Missing API_KEY environment variable")

HEADERS = {
    "X-Riot-Token": API_KEY
}