"""add embedding models to groups
Revision ID: 79994f41fa6e
Revises: de5ce1601c13
Create Date: 2023-12-01 15:04:46.218098
"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic
revision = "79994f41fa6e"
down_revision = "de5ce1601c13"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("assistants", "embedding_model")
    op.add_column(
        "groups",
        sa.Column(
            "uuid",
            postgresql.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
    )
    op.add_column("groups", sa.Column("embedding_model", sa.Text(), nullable=True))
    op.create_index(op.f("ix_groups_uuid"), "groups", ["uuid"], unique=True)
    op.drop_constraint("group_tenant_fk", "groups", type_="foreignkey")
    op.create_foreign_key(
        "group_tenant_fk",
        "groups",
        "tenants",
        ["tenant_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.create_index(
        op.f("ix_info_blobs_group_id"), "info_blobs", ["group_id"], unique=False
    )
    op.drop_constraint("info_blobs_group_id_fkey", "info_blobs", type_="foreignkey")
    op.create_foreign_key(
        "info_blobs_group_id_fkey",
        "info_blobs",
        "groups",
        ["group_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.add_column(
        "tenants", sa.Column("default_embedding_model", sa.Text(), nullable=True)
    )

    conn = op.get_bind()
    conn.execute(
        sa.text("UPDATE tenants SET default_embedding_model = 'text-embedding-ada-002'")
    )

    op.alter_column("tenants", "default_embedding_model", nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tenants", "default_embedding_model")
    op.drop_constraint("info_blobs_group_id_fkey", "info_blobs", type_="foreignkey")
    op.create_foreign_key(
        "info_blobs_group_id_fkey", "info_blobs", "groups", ["group_id"], ["id"]
    )
    op.drop_index(op.f("ix_info_blobs_group_id"), table_name="info_blobs")
    op.drop_constraint("group_tenant_fk", "groups", type_="foreignkey")
    op.create_foreign_key("group_tenant_fk", "groups", "tenants", ["tenant_id"], ["id"])
    op.drop_index(op.f("ix_groups_uuid"), table_name="groups")
    op.drop_column("groups", "embedding_model")
    op.drop_column("groups", "uuid")
    op.add_column(
        "assistants",
        sa.Column("embedding_model", sa.TEXT(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###