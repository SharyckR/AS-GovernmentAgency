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
    type: str = 'Legal entity'

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
        return 'Type: {0}'.format(self.type)
