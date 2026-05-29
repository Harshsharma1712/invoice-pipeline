from dataclasses import dataclass
from typing import Optional


@dataclass
class InformationItemCreate:
    particulars: str
    size: Optional[str]
    hsn_code: Optional[str]
    quantity: float
    quantity_unit: str
    rate: float
    item_total: float