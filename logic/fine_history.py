from pydantic import BaseModel
from typing import Optional
from logic.abstract_history import AbstractHistory


class FineHistory(AbstractHistory, BaseModel):
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

    dni_person: int = 123456789
    fine: Optional[str] = "Yes or No"
    type_fine: Optional[str] = "Type of Fine"
    description_fine: Optional[str] = "Description of the Fine"
    paid: Optional[str] = "Yes or No"
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def to_dict(self):
        fine_str = str(self.fine) if self.fine is not None else "None"
        type_fine_str = str(self.type_fine) if self.type_fine is not None else "None"
        description_fine_str = str(self.description_fine) if self.description_fine is not None else "None"
        paid_str = str(self.paid) if self.paid is not None else "None"
        return {
            "DNI Person": self.dni_person,
            "Fine?": fine_str,
            "Type of Fine": type_fine_str,
            "Description Fine": description_fine_str,
            "Paid?": paid_str
        }

    def __eq__(self, other):
        """ Returns bool of equality of history objects.
        :returns: bool history
        :rtype: bool
        """
        if isinstance(other, FineHistory):
            return (self.dni_person == other.dni_person and self.fine == other.fine and
                    self.type_fine == other.type_fine and self.description_fine == other.description_fine and
                    self.paid == other.paid)
        return False

    def __str__(self):
        """ Returns str of fine history.
        :returns: string fine history
        :rtype: str
        """

        fine_str = str(self.fine) if self.fine is not None else "None"
        type_fine_str = str(self.type_fine) if self.type_fine is not None else "None"
        description_fine_str = str(self.description_fine) if self.description_fine is not None else "None"
        paid_str = str(self.paid) if self.paid is not None else "None"

        return 'Dni: {0}, Has the person received a fine?: {1}, Type of the fine: {2}, Description of the fine: {3}, ' \
               'Has the person paid a fine?: {4}'.format(self.dni_person, fine_str, type_fine_str,
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
