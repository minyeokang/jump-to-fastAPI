"""empty message

Revision ID: 41b22c3b3667
Revises: b44a49fe3b8d
Create Date: 2023-04-06 16:53:24.454574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41b22c3b3667'
down_revision = 'b44a49fe3b8d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
