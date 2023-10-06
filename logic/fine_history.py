from pydantic import BaseModel


class FineHistory(BaseModel):
    """
     Class used to represent a Fine History

     Attributes:
            dni_person (int): DNI of the person to whom the history refers.
            fine (str): Has the person received a fine?
            type_fine (str): Type of the fine ( It depends on the answer, it will be mandatory or not ).
            description_fine (str): Description of the fine ( It depends on the answer, it will be mandatory or not ).
            paid (str): Has the person paid a fine? ( It depends on the answer, it will be mandatory or not ).
            mediator (str): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of a fine history.
            __eq__(other): Compares two objects fine history to check if they are equal.
    """

    dni_person: int = 0
    fine: str = "Yes or No"
    type_fine: str = "Type of Fine"
    description_fine: str = "Description of the Fine"
    paid: str = "Yes or No"
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def __eq__(self, another_history):
        """ Returns bool of equality of history objects.
        :returns: bool history
        :rtype: bool
        """
        return another_history.dni_person == self.dni_person

    def __str__(self):
        """ Returns str of fine history.
        :returns: string fine history
        :rtype: str
        """
        return 'Dni: {0}, Has the person received a fine?: {1}, Type of the fine: {2}, Description of the fine: {3}, ' \
               'Has the person paid a fine?: {4}'.format(self.dni_person, self.fine, self.type_fine,
                                                         self.description_fine, self.paid)
