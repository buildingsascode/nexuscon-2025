from pydantic import BaseModel


class Package(BaseModel):
    key: str
    vendor: str
    version: str
