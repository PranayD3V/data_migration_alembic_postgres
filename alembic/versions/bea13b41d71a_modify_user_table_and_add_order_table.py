"""modify user table and add order table

Revision ID: bea13b41d71a
Revises: e672f26878f3
Create Date: 2024-12-12 15:07:16.660856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'bea13b41d71a'
down_revision: Union[str, None] = 'e672f26878f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user', sa.Column('phone', sa.String, nullable=True))

    op.create_table(
        'order',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'), nullable=False),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id'), nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('order_date', sa.DateTime, server_default=sa.func.now())
    )


def downgrade() -> None:
    op.drop_table('order')
    op.drop_column('user', 'phone')

