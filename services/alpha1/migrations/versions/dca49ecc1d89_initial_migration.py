"""Initial migration

Revision ID: dca49ecc1d89
Revises:
Create Date: 2019-10-15 14:27:52.552230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dca49ecc1d89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    op.create_table(
        'organization',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    op.add_column(
        'user',
        sa.Column('organization_id', sa.Integer())
    )

    op.create_foreign_key(
        'org_fk', 'user', 'organization', ['organization_id'], ['id']
    )
    pass


def downgrade():
    pass
