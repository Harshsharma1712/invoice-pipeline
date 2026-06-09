from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Date

from app.database.db import Base


class Information(Base):
    __tablename__ = "information"

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String, unique=True, nullable=False)
    customer_name = Column(String, nullable=False)
    invoice_date = Column(Date, nullable=False)
    total_boxes = Column(Integer)
    total_pcs = Column(Integer)
    subtotal = Column(Float)
    discount_percentage = Column(Float)
    discount_amount = Column(Float)
    total = Column(Float)
    cgst_percentage = Column(Float)
    cgst_amount = Column(Float)
    sgst_percentage = Column(Float)
    sgst_amount = Column(Float)
    grand_total = Column(Float)

    pdf_url = Column(String)
    pdf_storage_path = Column(String)
    
    created_at = Column(
        DateTime, 
        default=datetime.now(timezone.utc)
    )
    # String-based relationship prevents circular imports across different files
    items = relationship(
        "InformationItem",
        back_populates="information",
        cascade="all, delete-orphan"
    )