"""2

Revision ID: f97d19eee7af
Revises: d41c05ad23e0
Create Date: 2019-11-15 16:29:06.813717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f97d19eee7af'
down_revision = 'd41c05ad23e0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'orgs',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )
    pass


def downgrade():
    pass
