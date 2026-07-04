from app.database.db import (
    SessionLocal
)

from app.models import (
    Information
)

from sqlalchemy.orm import Session

def save_pdf_metadata(
    invoice_id: int,
    # pdf_url: str,
    storage_path: str,
    db: Session
):

    # db = SessionLocal()

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

        # invoice.pdf_url = pdf_url

        invoice.pdf_storage_path = (
            storage_path
        )

        db.commit()
    
    except Exception as e:
        raise e

    # finally:

    #     db.close()
