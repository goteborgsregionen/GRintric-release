"""embedding_models settings
Revision ID: 4a1f5dd302ed
Revises: 9d3d6c1d04e8
Create Date: 2024-06-11 16:17:50.666974
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic
revision = "4a1f5dd302ed"
down_revision = "9d3d6c1d04e8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "embedding_model_settings",
        sa.Column("tenant_id", sa.Integer(), nullable=False),
        sa.Column("embedding_model_id", sa.UUID(), nullable=False),
        sa.Column("is_default", sa.Boolean(), server_default="False", nullable=False),
        sa.Column(
            "is_org_enabled", sa.Boolean(), server_default="False", nullable=False
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["embedding_model_id"], ["embedding_models.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["tenant_id"], ["tenants.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("tenant_id", "embedding_model_id"),
    )
    op.create_index(
        "embedding_model_is_default_unique",
        "embedding_model_settings",
        ["is_default", "tenant_id"],
        unique=True,
        postgresql_where=sa.text("is_default"),
    )
    op.drop_table("usergroups_embedding_models")
    op.add_column(
        "embedding_models",
        sa.Column(
            "is_deprecated", sa.Boolean(), server_default="False", nullable=False
        ),
    )
    op.drop_column("embedding_models", "selectable")
    op.drop_constraint("tenants_embedding_model_id_fkey", "tenants", type_="foreignkey")
    op.drop_column("tenants", "default_embedding_model_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "tenants",
        sa.Column(
            "default_embedding_model_id", sa.UUID(), autoincrement=False, nullable=True
        ),
    )
    op.create_foreign_key(
        "tenants_embedding_model_id_fkey",
        "tenants",
        "embedding_models",
        ["default_embedding_model_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.add_column(
        "embedding_models",
        sa.Column("selectable", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
    op.drop_column("embedding_models", "is_deprecated")
    op.create_table(
        "usergroups_embedding_models",
        sa.Column("embedding_model_id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("user_group_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["embedding_model_id"],
            ["embedding_models.id"],
            name="usergroups_embedding_models_embedding_model_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_group_id"],
            ["user_groups.id"],
            name="usergroups_embedding_models_user_group_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "embedding_model_id",
            "user_group_id",
            name="usergroups_embedding_models_pkey",
        ),
    )
    op.drop_index(
        "embedding_model_is_default_unique",
        table_name="embedding_model_settings",
        postgresql_where=sa.text("is_default"),
    )
    op.drop_table("embedding_model_settings")
    # ### end Alembic commands ###