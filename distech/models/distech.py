from abc import ABC, abstractmethod

from pydantic import BaseModel


class DistechResource(ABC, BaseModel):

    @classmethod
    @abstractmethod
    def get_endpoint(cls) -> str:
        pass
