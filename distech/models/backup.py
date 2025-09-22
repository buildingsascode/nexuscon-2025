import datetime

from pydantic import BaseModel, Field

from distech.models.package import Package
from distech.models.platform import Platform


class Backup(BaseModel):
    key: str
    size: int
    creation_time: datetime.datetime = Field(alias="creation-time")
    includes: list[str]
    packages: dict[str, "Package"]
    platform: "Platform"
