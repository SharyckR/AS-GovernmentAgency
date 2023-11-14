from typing import List

from logic.agency_factory import *
from logic.fine_history import *
from logic.vehicle_history import *


class TransportAgency(AgencyFactory):
    """
    Represents a transport agency.
    Attributes:
        agency (object): The associated agency factory.
        information_vehicles (List): Information about vehicles.
        information_fines (List): Information about fines.
    Methods:
        __str__(): Returns a formatted string with transport agency information.
        __eq__(other): Compares if two instances of TransportAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    agency.entity.subtype = "Transport Agency"
    information_vehicles: List[VehicleHistory] = [VehicleHistory()]
    information_fines: List[FineHistory] = [FineHistory()]

    def to_dict(self):
        information_vehicles = information_fines = []
        for information_vehicle in self.information_vehicles:
            information_vehicles.append(information_vehicle.to_dict())
        for information_fine in self.information_fines:
            information_fines.append(information_fine.to_dict())

        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(),
            "information_vehicles": information_vehicles,
            "information_fines": information_fines
            }
        }

    def __str__(self):
        """
        Returns a formatted string with transport agency information.
        :returns: string transport agency
        :rtype: str
        """
        information_vehicles = information_fines = ''
        for information_vehicle in self.information_vehicles:
            information_vehicles += information_vehicle.__str__() + ", "
        for information_fine in self.information_fines:
            information_fines += information_fine.__str__() + ", "
        return 'Agency: {0}, Information Vehicle: {1}, Information Fine: {2}\n'.format(
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
                    self.information_vehicle == other.information_vehicle and
                    self.information_fine == other.information_fine)


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
