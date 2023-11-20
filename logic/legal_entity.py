from typing import Union
from logic.entity import Entity


class LegalEntity(Entity):
    """
    Represents a legal entity.
    Attributes:
        type (str): The type of the entity.
        subtype (Union[str, None]): The subtype of the entity.
    Methods:
        to_dict() -> dict:
            Converts the LegalEntity instance to a dictionary.
        kind_of_entity() -> str:
            Returns the type of the entity.
        __str__() -> str:
            Returns a formatted string with entity information.
    """
    type: str = 'Legal Entity'
    subtype: Union[str, None] = None

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the legal entity.
        Returns:
            dict: A dictionary representation of the LegalEntity instance.
        """
        return {'type': self.type, 'subtype': self.subtype}

    def kind_of_entity(self) -> str:
        """
        Returns the type of the entity.
        Returns:
            str: The type of the entity.
        """
        return self.type

    def __str__(self) -> str:
        """
        Returns a formatted string with entity information.
        Returns:
            str: Formatted string with legal entity information.
        """
        return 'Type: {!r}, Subtype: {!r}'.format(self.type, self.subtype)
