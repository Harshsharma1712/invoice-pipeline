from dataclasses import dataclass
from typing import List, Optional

# Import the item schema for type hint resolution
from app.schemas.information_items import InformationItemCreate


@dataclass
class InformationCreate:
    invoice_number: str
    customer_name: str
    invoice_date: Optional[str]
    items: List[InformationItemCreate]
    total_boxes: int
    total_pcs: int
    subtotal: float
    discount_percentage: float
    discount_amount: float
    total: float
    cgst_percentage: float
    cgst_amount: float
    sgst_percentage: float
    sgst_amount: float
    grand_total: float