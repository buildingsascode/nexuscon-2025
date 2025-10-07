from pydantic import BaseModel


class Job(BaseModel):
    job: str
