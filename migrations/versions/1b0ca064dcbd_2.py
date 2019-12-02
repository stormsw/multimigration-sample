"""2

Revision ID: 1b0ca064dcbd
Revises: f97d19eee7af
Create Date: 2019-11-15 16:30:36.671997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b0ca064dcbd'
down_revision = 'd41c05ad23e0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )
    pass


def downgrade():
    pass
