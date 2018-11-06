"""empty message

Revision ID: 438fc0212962
Revises: a76d0bee246b
Create Date: 2018-10-31 23:11:26.750000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '438fc0212962'
down_revision = 'a76d0bee246b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('context', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###
