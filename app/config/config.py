import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    APP_NAME = "Invoice Digitization"

    DEBUG = True

    DATABASE_URL = os.getenv("DATABASE_URL")

    SUPABASE_URL = os.getenv("SUPABASE_URL")

    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    RESEND_API_KEY = os.getenv("RESEND_API_KEY")

    EMAIL_FROM = os.getenv(
        "EMAIL_FROM",
        "onboarding@resend.dev"
    )


settings = Settings()