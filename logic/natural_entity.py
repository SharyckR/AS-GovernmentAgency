from typing import Union
from logic.entity import Entity


class NaturalEntity(Entity):
    """
    Represents a natural entity.
    Attributes:
        type (str): The type of the entity, which is 'Natural Entity' in this case.
        subtype (Union[str, None]): The subtype of the natural entity, default is 'Person'.
    """
    type: str = 'Natural Entity'
    subtype: Union[str, None] = 'Person'

    def kind_of_entity(self):
        """
        Returns the type of the entity.
        Returns:
            str: The type of the entity.
        """
        return self.type

    def __str__(self):
        """
        Returns a formatted string representing the natural entity.
        Returns:
            str: Formatted string representing the natural entity.
        """
        return 'Type: {0}'.format(self.type)
