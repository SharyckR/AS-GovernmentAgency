from pydantic import BaseModel
from abc import ABC, abstractmethod


class Entity(ABC, BaseModel):
    """
    Abstract base class representing an Entity.

    Attributes:
        id_entity (int): The unique identifier for the entity.
        type (str): The type or category of the entity.

    Methods:
        kind_of_entity(): An abstract method that should be implemented by subclasses
                         to return the kind of entity.
    """
    id_entity: int = 0
    type: str = None

    @abstractmethod
    def kind_of_entity(self):
        """
        Abstract method to return the kind of entity.

        This method should be implemented by subclasses to provide the specific
        type or category of the entity.

        Returns:
            str: The kind or type of the entity.
        """
        pass
