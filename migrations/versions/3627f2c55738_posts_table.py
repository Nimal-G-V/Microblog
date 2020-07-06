"""Posts Table

Revision ID: 3627f2c55738
Revises: 26f3d2f75ee3
Create Date: 2020-07-06 18:25:03.954651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3627f2c55738'
down_revision = '26f3d2f75ee3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=True),
    sa.Column('time_stamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_time_stamp'), 'posts', ['time_stamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_time_stamp'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
