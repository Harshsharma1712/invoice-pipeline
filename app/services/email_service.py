import os
import resend

from base64 import b64encode

from app.config.config import (
    settings
)

resend.api_key = settings.RESEND_API_KEY


from app.models.information import Information


def send_invoice_email(
    invoice: Information,
    recipients: list[str],
    pdf_bytes: bytes
):

    resend.Emails.send({
        "from": settings.EMAIL_FROM,
        "to": recipients,
        "subject":
            f"Daily Sales Report - {invoice.invoice_date}",

        "html": f"""
        <h2>Daily Sales Report</h2>

        <p>
        Invoice Number:
        {invoice.invoice_number}
        </p>

        <p>
        Customer:
        {invoice.customer_name}
        </p>

        <p>
        Grand Total:
        ₹{invoice.grand_total}
        </p>
        """,

        "attachments": [
            {
                "filename":
                    f"{invoice.invoice_number}.pdf",

                "content":
                    b64encode(pdf_bytes).decode()
            }
        ]
    })