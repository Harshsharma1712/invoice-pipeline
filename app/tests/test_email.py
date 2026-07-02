from sqlalchemy import select

from app.database.db import SessionLocal

from app.models.information import Information

from app.services.generated_invoice_storage import (
    download_invoice_pdf
)

from app.services.email_service import (
    send_invoice_email
)


TEST_EMAILS = [
    "sharmahs017@gmail.com"
]


def get_test_invoice():

    session = SessionLocal()

    try:

        return session.scalar(
            select(Information)
            .order_by(Information.id.desc())
        )

    finally:
        session.close()


def test_email():

    invoice = get_test_invoice()

    if invoice is None:
        raise Exception(
            "No invoice found in database"
        )

    print(
        f"Invoice found: "
        f"{invoice.invoice_number}"
    )

    print(
        f"Storage path: "
        f"{invoice.pdf_storage_path}"
    )

    pdf_bytes = download_invoice_pdf(
        invoice.pdf_storage_path
    )

    print(
        f"Downloaded PDF size: "
        f"{len(pdf_bytes)} bytes"
    )

    send_invoice_email(
        invoice=invoice,
        recipients=TEST_EMAILS,
        pdf_bytes=pdf_bytes
    )

    print(
        "Email sent successfully"
    )


if __name__ == "__main__":
    test_email()