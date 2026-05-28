import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    APP_NAME = "Invoice Digitization"

    DEBUG = True


settings = Settings()