"""change invoice_date to date

Revision ID: 4b1dcbe424b9
Revises: b57a8c54483f
Create Date: 2026-06-05 18:59:49.520577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b1dcbe424b9'
down_revision: Union[str, Sequence[str], None] = 'b57a8c54483f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():

    op.execute("""
        ALTER TABLE information
        ALTER COLUMN invoice_date
        TYPE DATE
        USING TO_DATE(
            invoice_date,
            'DD/MM/YYYY'
        )
    """)


def downgrade():

    op.execute("""
        ALTER TABLE information
        ALTER COLUMN invoice_date
        TYPE VARCHAR
    """)
