from sqlalchemy import select

from app.database.db import SessionLocal
from app.models.user import User


def get_active_emails() -> list[str]:

    session = SessionLocal()

    try:

        users = session.scalars(
            select(User)
            .where(User.active == True)
        ).all()

        return [
            user.email
            for user in users
        ]

    finally:
        session.close()