import datetime
from typing import ClassVar, override

from pydantic import Field

from distech.models.distech import DistechResource
from distech.models.package import Package
from distech.models.platform import Platform


class Backup(DistechResource):
    ENDPOINT: ClassVar[str] = "/api/rest/v2/services/backup/backups/"

    key: str
    size: int
    creation_time: datetime.datetime = Field(alias="creation-time")
    includes: list[str]
    packages: dict[str, Package]
    platform: Platform

    @override
    @classmethod
    def get_endpoint(cls) -> str:
        return cls.ENDPOINT
