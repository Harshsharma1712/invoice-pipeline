from datetime import date
from pydantic import BaseModel


class InvoiceItemResponse(BaseModel):
    id: int
    particulars: str | None
    size: str | None
    hsn_code: str | None
    quantity: float | None
    quantity_unit: str | None
    rate: float | None
    item_total: float | None

    model_config = {
        "from_attributes": True
    }


class InvoiceResponse(BaseModel):
    id: int
    invoice_number: str
    customer_name: str
    invoice_date: date

    total_boxes: int | None
    total_pcs: int | None

    subtotal: float | None
    discount_percentage: float | None
    discount_amount: float | None

    total: float | None

    cgst_percentage: float | None
    cgst_amount: float | None

    sgst_percentage: float | None
    sgst_amount: float | None

    grand_total: float | None

    pdf_url: str | None

    items: list[InvoiceItemResponse]

    model_config = {
        "from_attributes": True
    }