from pydantic import BaseModel
from abc import ABC, abstractmethod


class Entity(ABC, BaseModel):
    type: str = None

    @abstractmethod
    def kind_of_entity(self):
        pass
