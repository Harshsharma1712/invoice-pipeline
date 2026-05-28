from PIL import Image

from google import genai

from app.config.config import settings
from app.config.constants import GEMINI_MODEL_NAME

from app.prompts.invoice_prompt import (
    INVOICE_EXTRACTION_PROMPT
)

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def extract_invoice_data(image_path: str):

    image = Image.open(image_path)

    response = client.models.generate_content(
        model=GEMINI_MODEL_NAME,
        contents=[
            INVOICE_EXTRACTION_PROMPT,
            image
        ]
    )

    return response.text