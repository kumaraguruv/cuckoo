# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

"""guest status

Revision ID: 1583656cb935
Revises: 1070cd314621
Create Date: 2015-12-15 14:25:27.379967

"""

# revision identifiers, used by Alembic.
revision = "1583656cb935"
down_revision = "1070cd314621"

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column("guests", sa.Column("status", sa.String(length=16), nullable=False, server_default="stopped"))

def downgrade():
    op.drop_column("guests", "status")
