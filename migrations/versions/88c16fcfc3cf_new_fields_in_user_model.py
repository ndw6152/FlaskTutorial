"""new fields in user model

Revision ID: 88c16fcfc3cf
Revises: d3d0a4953ac4
Create Date: 2018-04-22 20:21:21.770520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88c16fcfc3cf'
down_revision = 'd3d0a4953ac4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
