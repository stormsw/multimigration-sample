"""2

Revision ID: e7fc651a0f10
Revises: d41c05ad23e0
Create Date: 2019-11-15 16:41:28.382297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7fc651a0f10'
down_revision = 'd41c05ad23e0'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'analisys',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    pass


def downgrade():
    pass
