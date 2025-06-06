"""branches: added name field

Revision ID: df6b0e4a926d
Revises: 2a3b2f1a53c3
Create Date: 2025-05-25 22:54:31.015880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df6b0e4a926d'
down_revision: Union[str, None] = '2a3b2f1a53c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'company_branches',
        sa.Column(
            'name',
            sa.String(),
            nullable=True
        )
    )
    op.create_unique_constraint(None, 'company_branches', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'company_branches', type_='unique')
    op.drop_column('company_branches', 'name')
    # ### end Alembic commands ###
