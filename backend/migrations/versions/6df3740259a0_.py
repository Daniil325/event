"""empty message

Revision ID: 6df3740259a0
Revises: 
Create Date: 2024-05-26 12:50:34.101917

"""
from typing import Sequence, Union
from fastapi_storages import FileSystemStorage
from alembic import op
import sqlalchemy as sa
from fastapi_storages.integrations.sqlalchemy import FileType

# revision identifiers, used by Alembic.
revision: str = '6df3740259a0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
storage = FileSystemStorage(path="static")

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fio', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('dat', sa.Date(), nullable=True),
    sa.Column('event_type_id', sa.Integer(), nullable=True),
    sa.Column('file', FileType(storage=storage), nullable=True),
    sa.ForeignKeyConstraint(['event_type_id'], ['type_event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_in_event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member_in_event')
    op.drop_table('events')
    op.drop_table('users')
    op.drop_table('type_event')
    op.drop_table('member')
    op.drop_table('images')
    # ### end Alembic commands ###
