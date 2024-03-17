"""empty message

Revision ID: 4a5015e80b9e
Revises: a22a49c9203f
Create Date: 2024-03-16 23:14:06.343130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a5015e80b9e'
down_revision = 'a22a49c9203f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_title', sa.String(length=128), nullable=True),
    sa.Column('rooms_number', sa.Integer(), nullable=True),
    sa.Column('bathrooms_number', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('property_type', sa.String(length=128), nullable=True),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.Column('photo_filename', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###