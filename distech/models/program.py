import datetime
from typing import ClassVar, override

from pydantic import BaseModel, Field

from distech.models.distech import DistechResource


class DebugInfo(BaseModel):
    active: bool = Field(..., description="Indicates if debugging is active")
    last_start_time: str = Field(
        "", alias="last-start-time", description="Last start time of the debug session"
    )


class ProgramAuthor(BaseModel):
    computer_name: str = Field(
        alias="computer-name", description="Name of the computer that sent the program"
    )
    rest_user: str = Field(
        alias="rest-user", description="REST user who sent the program"
    )
    computer_user: str = Field(
        alias="computer-user", description="Computer user who sent the program"
    )


class ProjectInfo(BaseModel):
    identifier: str = Field(description="Unique identifier for the project")
    name: str = Field(description="Name of the project")
    version: str = Field(description="Version of the project")


class Program(DistechResource):
    """Model representing a GFX program on the Distech controller"""

    ENDPOINT: ClassVar[str] = "/api/rest/v2/services/gfx/programs/"

    key: str = Field(..., description="Unique identifier for the program")
    last_error: str = Field("", alias="last-error", description="Last error message")
    debug: DebugInfo = Field(description="Debug information about the program")
    sent_by: ProgramAuthor = Field(
        alias="sent-by", description="Information about the sender"
    )
    upload_date: datetime.datetime = Field(
        alias="upload-date", description="Upload date of the program"
    )
    project: ProjectInfo = Field(description="Project information")
    binary_hash: str = Field(..., alias="binary-hash", description="Hash of the binary")
    name: str = Field(..., description="Name of the program")
    state: str = Field(..., description="Current state of the program")

    @override
    @classmethod
    def get_endpoint(cls) -> str:
        return cls.ENDPOINT
