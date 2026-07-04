from fastapi import (
    APIRouter,
    Depends,
    File,
    UploadFile,
)

from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.api.schemas.invoice import InvoiceResponse
from app.api.services.invoice_service import (
    upload_invoice,
    get_invoice,
    get_invoices,
    delete_invoice,
)

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"],
)

# upload invoice and do all the process right now in single endpoint in future change and optmize this using celerly
@router.post(
    "/upload",
    response_model=InvoiceResponse,
)
def upload(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return upload_invoice(file, db)


# get invoice by id
@router.get(
    "/{invoice_id}",
    response_model=InvoiceResponse,
)
def get_by_id(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    return get_invoice(invoice_id, db)


# get all invoices
@router.get(
    "",
    response_model=list[InvoiceResponse],
)
def get_all(
    db: Session = Depends(get_db),
):
    return get_invoices(db)

# delete the invoice by id
@router.delete(
    "/{invoice_id}",
    status_code=204,
)
def delete(
    invoice_id: int,
    db: Session = Depends(get_db),
):
    delete_invoice(invoice_id, db)