"""added songs

Revision ID: 0707d88d09b7
Revises: 028fbaa122a5
Create Date: 2023-10-18 12:58:57.344212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0707d88d09b7'
down_revision = '028fbaa122a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_songs'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs')
    # ### end Alembic commands ###
