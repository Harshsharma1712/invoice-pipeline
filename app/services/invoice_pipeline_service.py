import os

from app.services.extraction_service import (
    process_invoice
)

from app.services.information_storage_service import (
    save_information
)

from app.services.invoice_generation_service import (
    generate_invoice
)

from app.services.generated_invoice_storage import (
    upload_invoice_pdf
)

from app.services.invoice_update_service import (
    save_pdf_metadata
)


def process_invoice_pipeline(
    image_path: str
):

    extracted_data = process_invoice(
        image_path
    )

    invoice = save_information(
        extracted_data
    )

    pdf_path = generate_invoice(
        invoice.invoice_number
    )

    upload_result = (
        upload_invoice_pdf(
            pdf_path,
            invoice.invoice_number
        )
    )

    save_pdf_metadata(
        invoice.id,
        upload_result["url"],
        upload_result["storage_path"]
    )

    if os.path.exists(
        pdf_path
    ):
        os.remove(
            pdf_path
        )

    return upload_result