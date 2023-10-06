"""empty message

Revision ID: 66a7172bd294
Revises: 5a87384f8486
Create Date: 2023-10-05 23:48:29.162575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66a7172bd294'
down_revision: Union[str, None] = '5a87384f8486'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_storage_id'), 'storage', ['id'], unique=False)
    op.create_table('inputs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('storage_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['storage_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inputs_id'), 'inputs', ['id'], unique=False)
    op.create_table('outputs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('storage_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['storage_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_outputs_id'), 'outputs', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_outputs_id'), table_name='outputs')
    op.drop_table('outputs')
    op.drop_index(op.f('ix_inputs_id'), table_name='inputs')
    op.drop_table('inputs')
    op.drop_index(op.f('ix_storage_id'), table_name='storage')
    op.drop_table('storage')
    # ### end Alembic commands ###