# Copyright 2025 Canonical Ltd.
# See LICENSE file for licensing details.
"""Skeleton for the abstract charm."""

from .config.config import CharmConfig
from .config.literals import SYSTEM_USERS, USER
from .lib.charms.data_platform_libs.v1.data_models import TypedCharmBase
from .utils.postgresql import PostgreSQL


class AbstractPostgreSQLCharm(TypedCharmBase[CharmConfig]):
    """An abstract PostgreSQL charm."""

    def __init__(self, *args):
        super().__init__(*args)

        self.postgresql = PostgreSQL(
            primary_host="",
            current_host="",
            user=USER,
            password="",
            database="",
            system_users=SYSTEM_USERS,
        )
