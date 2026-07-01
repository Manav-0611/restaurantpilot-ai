from dotenv import load_dotenv
import os

# Load values from the .env file
load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

DATABASE_URL = os.getenv("DATABASE_URL")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

SECRET_KEY = os.getenv("SECRET_KEY")