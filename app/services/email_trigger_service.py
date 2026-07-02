from app.services.user_query_service import (
    get_active_emails
)

from app.services.email_service import (
    send_invoice_email
)

from app.services.generated_invoice_storage import (
    download_invoice_pdf
)


def trigger_daily_invoice_email(
    invoice
):

    recipients = get_active_emails()

    if not recipients:
        return

    pdf_bytes = download_invoice_pdf(
        invoice.pdf_storage_path
    )

    send_invoice_email(
        invoice=invoice,
        recipients=recipients,
        pdf_bytes=pdf_bytes
    )
