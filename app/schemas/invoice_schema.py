from pydantic import BaseModel
from typing import List, Optional


class InvoiceItem(BaseModel):
    particulars: str
    size: Optional[str]
    hsn_code: Optional[str]
    box_pcs: float
    rate: float
    vatable_amount: float


class InvoiceData(BaseModel):

    customer_name: Optional[str]

    invoice_name: Optional[str]

    items: List[InvoiceItem]


class FinalInvoiceData(InvoiceData):

    invoice_number: str

    total_boxes: float

    subtotal: float

    tax_amount: float

    grand_total: float