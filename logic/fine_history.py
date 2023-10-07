from pydantic import BaseModel
from typing import Optional


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

    dni_person: int = 1
    fine: str = "Yes or No"
    type_fine: Optional[str] = "Type of Fine"
    description_fine: Optional[str] = "Description of the Fine"
    paid: Optional[str] = "Yes or No"
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

        type_fine_str = str(self.type_fine) if self.type_fine is not None else "None"
        description_fine_str = str(self.description_fine) if self.description_fine is not None else "None"
        paid_str = str(self.paid) if self.paid is not None else "None"

        return 'Dni: {0}, Has the person received a fine?: {1}, Type of the fine: {2}, Description of the fine: {3}, ' \
               'Has the person paid a fine?: {4}'.format(self.dni_person, self.fine, type_fine_str,
                                                         description_fine_str, paid_str)


if __name__ == '__main__':
    # Prueba Fine History class

    fine_history1 = FineHistory(dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                                description_fine="The person was going more than 100k/h", paid="No")

    fine_history2 = FineHistory(dni_person=45761873, fine="No", type_fine=None, description_fine=None, paid=None)

    fine_history1_str = fine_history1.__str__()
    print(f"Fine 1 Information \n {fine_history1_str}")
    fine_history2_str = fine_history2.__str__()
    print(f"Fine 2 Information \n {fine_history2_str}")

    are_equal_fine_history = fine_history1.__eq__(fine_history2)
    print(f"Are equals ? \n {are_equal_fine_history} \n\n")

fine_history1 = FineHistory(dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                            description_fine="The person was going more than 100k/h", paid="No")
fine_history2 = FineHistory(dni_person=45761873, fine="No", type_fine=None, description_fine=None, paid=None)
