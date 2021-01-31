"""add user

Revision ID: 3c17ebae6c71
Revises: dd83fe8e1c04
Create Date: 2021-01-30 19:43:23.241970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c17ebae6c71'
down_revision = 'dd83fe8e1c04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('update_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('login', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.VARBINARY(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login')
    )
    op.add_column('employees', sa.Column('user_id', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employees', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
