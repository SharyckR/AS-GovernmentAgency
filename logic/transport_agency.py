from typing import List

from logic.agency_factory import *
from logic.fine_history import *
from logic.vehicle_history import *


class TransportAgency(AgencyFactory):
    """
    Represents a transport agency.
    Attributes:
        agency (object): The associated agency factory.
        information_vehicles (List[VehicleHistory]): Information about vehicles.
        information_fines (List[FineHistory]): Information about fines.
    Methods:
        to_dict(): Converts the TransportAgency object to a dictionary.
        __str__(): Returns a formatted string with transport agency information.
        __eq__(other): Compares if two instances of TransportAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    agency.entity.subtype = "Transport Agency"
    information_vehicles: List[VehicleHistory] = []
    information_fines: List[FineHistory] = []

    def to_dict(self):
        """
        Returns a dictionary representation of the transport agency.
        Returns:
            dict: Dictionary representation of the TransportAgency object.
        """
        information_vehicles = [info.to_dict() for info in self.information_vehicles]
        information_fines = [info.to_dict() for info in self.information_fines]
        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(), "information_vehicles": information_vehicles,
            "information_fines": information_fines}}

    def __str__(self):
        """
        Returns a formatted string with transport agency information.
        Returns:
            str: Formatted string representing the TransportAgency object.
        """
        information_vehicles = ', '.join(str(info) for info in self.information_vehicles)
        information_fines = ', '.join(str(info) for info in self.information_fines)
        return 'Agency: {0}, Information Vehicles: {1}, Information Fines: {2}\n'.format(
            self.agency, information_vehicles, information_fines)

    def __eq__(self, other):
        """
        Compares if two instances of TransportAgency are equal.
        Args:
            other (TransportAgency): The other instance to compare.
        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, TransportAgency):
            return (self.agency == other.agency and
                    self.information_vehicles == other.information_vehicles and
                    self.information_fines == other.information_fines)


if __name__ == '__main__':
    transport1 = TransportAgency(agency=agency1, information_vehicles=[vehicle_history1],
                                 information_fines=[fine_history1])
    transport2 = TransportAgency(agency=agency2, information_vehicles=[vehicle_history2],
                                 information_fines=[fine_history2])
    print(f"Transport Agency 1 Information \n {transport1}")
    print(f"Transport Agency 2 Information \n {transport2}")
    are_equal_transport_agency = transport1.__eq__(transport2)
    print(f"Are equals ? \n {are_equal_transport_agency} \n\n")

transport1 = TransportAgency(agency=agency1, information_vehicles=[vehicle_history1], information_fines=[fine_history1])
transport2 = TransportAgency(agency=agency2, information_vehicles=[vehicle_history2], information_fines=[fine_history2])
