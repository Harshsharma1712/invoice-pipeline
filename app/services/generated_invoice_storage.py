from app.config.config import settings

from supabase import create_client

supabase = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_ROLE_KEY
)

def upload_invoice_pdf(
        pdf_path: str,
        invoice_number: str
):
    storage_path = (
        f"invoices/{invoice_number}.pdf"
    )

    with open(
        pdf_path,
        "rb"
    ) as f:

        supabase.storage.from_(
        "invoices"
    ).upload(
        storage_path,
        f.read(),
        {
            "content-type": "application/pdf"
        }
    )

    signed_url = (
    supabase.storage
    .from_("invoices")
    .create_signed_url(
        storage_path,
        3600
    )
)

    return {
        "storage_path": storage_path,
        "url": signed_url["signedURL"]
    }


def download_invoice_pdf(
        storage_path: str
):
    response = (
        supabase.storage
        .from_("invoices")
        .download(storage_path)
    )

    return response
