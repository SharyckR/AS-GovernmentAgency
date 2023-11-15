from typing import Union
from logic.entity import Entity


class LegalEntity(Entity):
    """
    Represents a legal entity.
    Attributes:
        type (str): The type of the entity.

    Methods:
        kind_of_entity(): Returns the type of the entity.
        __str__(): Returns a formatted string with entity information.
    """
    type: str = 'Legal Entity'
    subtype: Union[str, None] = None

    def to_dict(self):
        return {'type': self.type, 'subtype': self.subtype}

    def kind_of_entity(self):
        """
        Returns the type of the entity.
        Returns:
            str: The type of the entity.
        """
        return self.type

    def __str__(self):
        """ Returns str of legal entity.
        :returns: string legal entity
        :rtype: str
        """
        return 'Type: {!r}, Subtype: {!r}'.format(self.type, self.subtype)
