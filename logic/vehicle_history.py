from pydantic import BaseModel
from typing import Optional


class VehicleHistory(BaseModel):
    """
    Class to represent vehicle history.

    Attributes:
        dni_person (object): DNI of the person associated with the vehicle.
        licence (str) : Does the person have a license?.
        type_licence : Type of license of the person ( if they have one ).
        vehicle (str): Does the person have a vehicle?.
        type_vehicle (str): Type of vehicle of the person ( if they have one ).
        description_vehicle (str): A description or additional information about the vehicle.
        plate_vehicle (str): The license plate number of the vehicle.

    Methods:
        __str__(): Returns a string representation of the VehicleHistory object.
        __eq__(other): Compares two VehicleHistory objects to check if they are equal.
    """

    dni_person: int = 0
    licence: str = "Yes or No"
    type_licence: Optional[str] = "A1 or A2 or B1 or B2 or B3 or C1 or C2 or C3"
    vehicle: str = "Yes or No"
    type_vehicle: Optional[str] = "Car or Motorcycle"
    description_vehicle: Optional[str] = "Description of the Vehicle"
    plate_vehicle: Optional[str] = "Plate of the vehicle"
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def __str__(self) -> str:
        """
        Returns a string representation of the Vehicle History object.
        """
        type_licence_str = str(self.type_licence) if self.type_licence is not None else "None"
        type_vehicle_str = str(self.type_vehicle) if self.type_vehicle is not None else "None"
        description_vehicle_str = str(self.description_vehicle) if self.description_vehicle is not None else "None"
        plate_vehicle = str(self.plate_vehicle) if self.plate_vehicle is not None else "None"

        return '(Dni: {0}, Does the person have a license?: {1}, Type of license: {2},' \
               'Does the person have a vehicle?: {3}, Type of vehicle: {4}, Description of the Vehicle: {5},' \
               'Plate of the vehicle: {6})'.format(self.dni_person, self.licence, type_licence_str, self.vehicle,
                                                   type_vehicle_str, description_vehicle_str, plate_vehicle)

    def __eq__(self, other) -> bool:
        """
        Compares two VehicleHistory objects to check if they are equal.

        Args:
            other (VehicleHistory): Another VehicleHistory object to compare.

        Returns:
            bool: True if the VehicleHistory objects are equal, False otherwise.
        """
        if isinstance(other, VehicleHistory):
            return (self.dni_person == other.dni_person and self.licence == other.licence and
                    self.type_licence == other.type_licence and self.vehicle == other.vehicle and
                    self.type_vehicle == other.type_vehicle and
                    self.description_vehicle == other.description_vehicle and
                    self.plate_vehicle == other.plate_vehicle)
        else:
            return False
