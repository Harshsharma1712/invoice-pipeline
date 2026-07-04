from sqlalchemy import select

from app.database.db import SessionLocal
from app.models.user import User

from sqlalchemy.orm import Session


def get_active_emails(
        db: Session
) -> list[str]:

    # session = SessionLocal()

    try:

        users = db.scalars(
            select(User)
            .where(User.active == True)
        ).all()

        return [
            user.email
            for user in users
        ]
    
    except Exception as e:
        raise e

    # finally:
    #     db.close()