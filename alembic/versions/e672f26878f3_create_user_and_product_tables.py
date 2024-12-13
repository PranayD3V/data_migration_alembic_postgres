"""create user and product tables

Revision ID: e672f26878f3
Revises: 
Create Date: 2024-12-12 14:59:12.543952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e672f26878f3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, unique=True, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )


    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('price', sa.Numeric, nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('product')
    op.drop_table('user')