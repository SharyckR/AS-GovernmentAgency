from typing import Union
from pydantic import BaseModel
from abc import ABC, abstractmethod


class Entity(ABC, BaseModel):
    """
    Abstract base class representing an Entity.
    Attributes:
        username (Union[str, None]): The identifier for the entity.
        email (Union[str, None]): The email address associated with the entity.
        disabled (bool): A flag indicating whether the entity is disabled or not.
    Methods:
        kind_of_entity() -> str:
            An abstract method that should be implemented by subclasses
            to return the kind of entity.
    """
    username: Union[str, None] = None
    email: Union[str, None] = None
    disabled: bool = False

    @abstractmethod
    def kind_of_entity(self) -> str:
        """
        Abstract method to return the kind of entity.
        This method should be implemented by subclasses to provide the specific
        type or category of the entity.
        Returns:
            str: The kind or type of the entity.
        """
        pass
