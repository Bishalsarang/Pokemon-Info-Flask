"""empty message

Revision ID: 3587ad21cf2a
Revises: 
Create Date: 2020-01-15 13:04:33.199981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3587ad21cf2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image_link', sa.String(length=20), nullable=True),
    sa.Column('height', sa.String(length=20), nullable=True),
    sa.Column('category', sa.String(length=20), nullable=True),
    sa.Column('weight', sa.String(length=20), nullable=True),
    sa.Column('abilities', sa.String(length=20), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('pokemon_id')
    )
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weakness',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weakness', sa.String(length=20), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weakness')
    op.drop_table('type')
    op.drop_table('pokemon')
    # ### end Alembic commands ###