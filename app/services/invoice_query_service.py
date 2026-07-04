from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.models import Information
from app.services.generated_invoice_storage import get_invoice_signed_url


def get_invoice_by_number(
    db: Session,
    invoice_number: str
):
    return (
        db.query(Information)
        .options(
            selectinload(
                Information.items
            )
        )
        .filter(
            Information.invoice_number == invoice_number
        )
        .first()
    )


def get_invoices_by_date(
    db: Session,
    invoice_date: date
):
    return (
        db.query(Information)
        .options(
            selectinload(
                Information.items
            )
        )
        .filter(
            Information.invoice_date == invoice_date
        )
        .all()
    )


from sqlalchemy import select

from app.models.information import Information
from app.database.db import SessionLocal

def get_invoice_by_id(
    invoice_id: int,
    db: Session
):

    # session = SessionLocal()

    try:

        invoice = db.scalar(
            select(Information)
            .where(
                Information.id == invoice_id
            )
        )

        if invoice and invoice.pdf_storage_path:
            invoice.pdf_url = get_invoice_signed_url(
                invoice.pdf_storage_path
            )
        
        return invoice
    
    except Exception as e:
        raise e

    # finally:
    #     db.close()


# def get_invoice_by_id(
#     invoice_id: int,
#     db: Session,
# ):
#     """
#     Fetch a single invoice by its ID.
#     """

#     return (
#         db.query(Information)
#         .filter(Information.id == invoice_id)
#         .first()
#     )


def get_all_invoices(
    db: Session,
):
    """
    Fetch all invoices ordered by newest first.
    """

    
    invoices = db.query(Information).order_by(Information.created_at.desc()).all()

    for invoice in invoices:
        if invoice.pdf_storage_path:
            invoice.pdf_url = get_invoice_signed_url(
                invoice.pdf_storage_path
            )
    
    return invoices

    


def delete_invoice(
    invoice_id: int,
    db: Session,
):
    """
    Delete an invoice and all of its items.

    Returns:
        True  -> Invoice deleted
        False -> Invoice not found
    """

    invoice = (
        db.query(Information)
        .filter(Information.id == invoice_id)
        .first()
    )

    if invoice is None:
        return False

    try:

        db.delete(invoice)

        db.commit()

        return True

    except Exception:

        db.rollback()

        raise