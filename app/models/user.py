from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        nullable=False,
        unique=True
    )

    active = Column(
        Boolean,
        default=True
    )