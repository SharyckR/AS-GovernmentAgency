from logic.entity import Entity


class NaturalEntity(Entity):
    """
    Represents a natural entity.

    Attributes:
        type (str): The type of the entity, which is 'Natural Entity' in this case.

    Methods:
        kind_of_entity(): Returns the type of the entity.
        __str__(): Returns a formatted string representing the natural entity.

    """
    type: str = 'Natural Entity'

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

        :returns: string natural entity
        :rtype: str
        """
        return 'Type: {0}'.format(self.type)
