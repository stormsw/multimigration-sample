"""2nd migration

Revision ID: 1c930b067e85
Revises: dca49ecc1d89
Create Date: 2019-10-15 16:21:50.014275

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c930b067e85'
down_revision = 'dca49ecc1d89'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'test_schema.user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )
    pass


def downgrade():
    pass
