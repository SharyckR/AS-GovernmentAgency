from pydantic import BaseModel


class VehicleHistory(BaseModel):
    """
    Class to represent vehicle history.

    Attributes:
        information_person (object): Information about the person associated with the vehicle.
        vehicle (str): The make or manufacturer of the vehicle.
        type_vehicle (str): The type or category of the vehicle.
        description_vehicle (str): A description or additional information about the vehicle.
        plate_vehicle (str): The license plate number of the vehicle.

    Methods:
        __str__(): Returns a string representation of the VehicleHistory object.
        __eq__(other): Compares two VehicleHistory objects to check if they are equal.
    """

    information_person: str  # Information about the person associated with the vehicle
    vehicle: str  # The make or manufacturer of the vehicle
    type_vehicle: str  # The type or category of the vehicle
    description_vehicle: str  # A description or additional information about the vehicle
    plate_vehicle: str  # The license plate number of the vehicle

    def __str__(self) -> str:
        """
        Returns a string representation of the VehicleHistory object.
        """
        return '({0},{1},{2},{3},{4})'.format(
            self.information_person, self.vehicle, self.type_vehicle,
            self.description_vehicle, self.plate_vehicle
        )

    def __eq__(self, other) -> bool:
        """
        Compares two VehicleHistory objects to check if they are equal.

        Args:
            other (VehicleHistory): Another VehicleHistory object to compare.

        Returns:
            bool: True if the VehicleHistory objects are equal, False otherwise.
        """
        if isinstance(other, VehicleHistory):
            return (self.information_person == other.information_person and self.vehicle == other.vehicle and
                    self.type_vehicle == other.type_vehicle and
                    self.description_vehicle == other.description_vehicle and
                    self.plate_vehicle == other.plate_vehicle)
        else:
            return False


if __name__ == '__main__':
    vehicleH1 = VehicleHistory(information_person='Person()', vehicle='Y', type_vehicle='Toyota',
                               description_vehicle='Red and small', plate_vehicle='10200220')
    vehicleH2 = VehicleHistory(information_person='Person()', vehicle='Y', type_vehicle='Ferrari',
                               description_vehicle='black and large', plate_vehicle='1020030')
    print(vehicleH1.__str__())
    print(vehicleH1.__eq__(vehicleH2))
