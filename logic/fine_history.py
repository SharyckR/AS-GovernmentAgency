from pydantic import BaseModel
from typing import Union
from logic.abstract_history import AbstractHistory


class FineHistory(AbstractHistory, BaseModel):
    """
    Class used to represent a Fine History.
    Attributes:
        id_history (int): The identifier for the fine history.
        dni_person (int): DNI of the person to whom the history refers.
        fine (Union[str, None]): Has the person received a fine?
        type_fine (Union[str, None]): Type of the fine (It depends on the answer, it will be mandatory or not).
        description_fine (Union[str, None]): Description of the fine (It depends on the answer, it will be mandatory or not).
        paid (Union[str, None]): Has the person paid a fine? (It depends on the answer, it will be mandatory or not).
        mediator (Union[object, None]): Mediator for managing interactions.
    Methods:
        __init__(mediator=None, **data): Initializes a FineHistory instance.
        __str__(): Returns a string representation of a fine history.
        __eq__(other): Compares two FineHistory objects for equality.
        to_dict(): Returns a dictionary representation of the fine history.
    """
    id_history: int = 1
    dni_person: int = 123456789
    fine: Union[str, None] = "Yes or No"
    type_fine: Union[str, None] = "Type of Fine"
    description_fine: Union[str, None] = "Description of the Fine"
    paid: Union[str, None] = "Yes or No"
    mediator: Union[object, None] = None

    def __init__(self, mediator=None, **data):
        """
        Initializes a FineHistory instance.
        Args:
            mediator (object, optional): Mediator for managing interactions.
            **data: Additional keyword arguments for initializing the attributes.
        Returns:
            None
        """
        super().__init__(**data)
        self.mediator = mediator

    def to_dict(self):
        """
        Returns a dictionary representation of the fine history.
        Returns:
            dict: Dictionary representation of the fine history.
        """
        fine_str = str(self.fine) if self.fine is not None else "None"
        type_fine_str = str(self.type_fine) if self.type_fine is not None else "None"
        description_fine_str = str(self.description_fine) if self.description_fine is not None else "None"
        paid_str = str(self.paid) if self.paid is not None else "None"
        return {
            str(self.dni_person): {
                "id_history": self.id_history, "fine": fine_str, "type_fine": type_fine_str,
                "description_fine": description_fine_str, "paid": paid_str}}

    def __eq__(self, other):
        """
        Compares two FineHistory objects for equality.
        Args:
            other (FineHistory): The other instance to compare.
        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, FineHistory):
            return (
                self.id_history == other.id_history and self.dni_person == other.dni_person and
                self.fine == other.fine and self.type_fine == other.type_fine and
                self.description_fine == other.description_fine and self.paid == other.paid)
        return False

    def __str__(self):
        """
        Returns a string representation of a fine history.
        Returns:
            str: String representation of the fine history.
        """
        fine_str = str(self.fine) if self.fine is not None else "None"
        type_fine_str = str(self.type_fine) if self.type_fine is not None else "None"
        description_fine_str = str(self.description_fine) if self.description_fine is not None else "None"
        paid_str = str(self.paid) if self.paid is not None else "None"
        return (
            'ID History: {!r}, Dni: {!r}, Has the person received a fine?: {!r}, Type of the fine: {!r}, '
            'Description of the fine: {!r}, Has the person paid a fine?: {!r}\n'
        ).format(self.id_history, self.dni_person, fine_str, type_fine_str, description_fine_str, paid_str)


if __name__ == '__main__':
    # Prueba Fine History class
    fine_history1 = FineHistory(
        id_history=14, dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
        description_fine="The person was going more than 100k/h", paid="No")
    fine_history2 = FineHistory(
        id_history=12, dni_person=45761873, fine="No", type_fine=None, description_fine=None, paid=None)
    fine_history1_str = fine_history1.__str__()
    print(f"Fine 1 Information \n {fine_history1_str}")
    fine_history2_str = fine_history2.__str__()
    print(f"Fine 2 Information \n {fine_history2_str}")
    are_equal_fine_history = fine_history1.__eq__(fine_history2)
    print(f"Are equals ? \n {are_equal_fine_history} \n\n")


fine_history1 = FineHistory(id_history=14, dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                            description_fine="The person was going more than 100k/h", paid="No")
fine_history2 = FineHistory(id_history=12, dni_person=45761873, fine="No", type_fine=None, description_fine=None,
                            paid=None)
