from app.database.db import (
    SessionLocal
)

from app.models import (
    Information
)

def save_pdf_metadata(
    invoice_id: int,
    pdf_url: str,
    storage_path: str
):

    db = SessionLocal()

    try:

        invoice = (
            db.query(
                Information
            )
            .filter(
                Information.id == invoice_id
            )
            .first()
        )

        invoice.pdf_url = pdf_url

        invoice.pdf_storage_path = (
            storage_path
        )

        db.commit()

    finally:

        db.close()
