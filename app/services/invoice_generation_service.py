from datetime import date

from app.database.db import (
    SessionLocal
)

from app.services.invoice_query_service import (
    get_invoice_by_number,
    get_invoices_by_date
)

from app.services.pdf_invoice_service import (
    generate_invoice_pdf
)

def generate_invoice_from_object(invoice):
    return generate_invoice_pdf(invoice)


def generate_invoice(
    invoice_number: str
):
    db = SessionLocal()

    try:

        invoice = get_invoice_by_number(
            db,
            invoice_number
        )

        if not invoice:

            raise ValueError(
                f"Invoice {invoice_number} not found"
            )

        return generate_invoice_pdf(
            invoice
        )

    finally:

        db.close()


def generate_daily_invoices(
    invoice_date: date
):
    db = SessionLocal()

    try:

        invoices = get_invoices_by_date(
            db,
            invoice_date
        )

        pdf_files = []

        for invoice in invoices:

            pdf_path = (
                generate_invoice_pdf(
                    invoice
                )
            )

            pdf_files.append(
                pdf_path
            )

        return pdf_files

    finally:

        db.close()