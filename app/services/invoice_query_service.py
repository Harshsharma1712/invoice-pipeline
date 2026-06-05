from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy.orm import selectinload

from app.models import Information


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