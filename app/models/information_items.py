from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database.db import Base


class InformationItem(Base):
    __tablename__ = "information_items"

    id = Column(Integer, primary_key=True)
    information_id = Column(
        Integer, 
        ForeignKey("information.id"), 
        nullable=False
    )
    
    particulars = Column(String)
    size = Column(String)
    hsn_code = Column(String)
    quantity = Column(Float)
    quantity_unit = Column(String)
    rate = Column(Float)
    item_total = Column(Float)
    
    created_at = Column(
        DateTime, 
        default=datetime.now(timezone.utc)
    )

    # String-based relationship points smoothly back to the Information class
    information = relationship(
        "Information", 
        back_populates="items"
    )