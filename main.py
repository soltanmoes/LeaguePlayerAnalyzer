import os
from dotenv import load_dotenv

load_dotenv() # reads variables from a .env file and sets them in os.environ
API_KEY = os.getenv("API_KEY")

