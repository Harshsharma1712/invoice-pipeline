import os
import shutil
import tempfile

from fastapi import (
    HTTPException,
    UploadFile,
)

from sqlalchemy.orm import Session

from app.services.extraction_service import process_invoice
from app.services.information_storage_service import save_information
from app.services.invoice_generation_service import generate_invoice
from app.services.generated_invoice_storage import upload_invoice_pdf
from app.services.invoice_update_service import save_pdf_metadata
from app.services.invoice_query_service import (
    get_invoice_by_id,
    get_all_invoices,
    delete_invoice as delete_invoice_db,
)
from app.services.email_trigger_service import trigger_daily_invoice_email

def upload_invoice(
    file: UploadFile,
    db: Session,
):

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp:

        shutil.copyfileobj(
            file.file,
            temp,
        )

        temp_path = temp.name

    try:

        extracted = process_invoice(
            temp_path
        )

        invoice = save_information(
            extracted,
            db,
        )

        pdf_path = generate_invoice(
            invoice.invoice_number,
            db
        )

        upload_result = upload_invoice_pdf(
            pdf_path,
            invoice.invoice_number,
        )

        save_pdf_metadata(
            invoice.id,
            # upload_result["url"],
            upload_result["storage_path"],
            db,
        )

        invoice = get_invoice_by_id(
            invoice.id,
            db,
        )
    
        trigger_daily_invoice_email(
            invoice, 
            db
        )

        return invoice
    

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)


# get invoice by id
def get_invoice(
    invoice_id: int,
    db: Session,
):

    invoice = get_invoice_by_id(
        invoice_id,
        db,
    )

    if invoice is None:

        raise HTTPException(
            status_code=404,
            detail="Invoice not found",
        )

    return invoice


# get all invoice
def get_invoices(
    db: Session,
):

    return get_all_invoices(db)

# delete invoice by id
def delete_invoice(
    invoice_id: int,
    db: Session,
):

    deleted = delete_invoice_db(
        invoice_id,
        db,
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Invoice not found",
        )

