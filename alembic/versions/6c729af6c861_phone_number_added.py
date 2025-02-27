"""phone number added

Revision ID: 6c729af6c861
Revises: 
Create Date: 2025-02-27 15:19:22.109085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '6c729af6c861'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String, nullable=True))


def downgrade() -> None:
    #op.drop_column("users", "phone_number")
    pass
