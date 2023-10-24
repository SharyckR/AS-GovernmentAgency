from logic.agency_factory import *
from logic.fine_history import *
from logic.vehicle_history import *


class TransportAgency(AgencyFactory):
    """
    Represents a transport agency.

    Attributes:
        agency (object): The associated agency factory.
        information_vehicle (object): Information about vehicles.
        information_fine (object): Information about fines.

    Methods:
        __str__(): Returns a formatted string with transport agency information.
        __eq__(other): Compares if two instances of TransportAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    information_vehicle: VehicleHistory = VehicleHistory()
    information_fine: FineHistory = FineHistory()

    def to_dict(self):
        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(),
            "information_vehicle": self.information_vehicle.to_dict(),
            "information_fine": self.information_fine.to_dict()
            }
        }

    def __str__(self):
        """
        Returns a formatted string with transport agency information.
        :returns: string transport agency
        :rtype: str
        """
        return 'Agency: {0}, Information Vehicle: {1}, Information Fine: {2}'.format(
            self.agency, self.information_vehicle, self.information_fine)

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
    transport1 = TransportAgency(agency=agency1, information_vehicle=vehicle_history1, information_fine=fine_history1)
    transport2 = TransportAgency(agency=agency2, information_vehicle=vehicle_history2, information_fine=fine_history2)

    print(f"Transport Agency 1 Information \n {transport1}")
    print(f"Transport Agency 2 Information \n {transport2}")

    are_equal_transport_agency = transport1.__eq__(transport2)
    print(f"Are equals ? \n {are_equal_transport_agency} \n\n")

transport1 = TransportAgency(agency=agency1, information_vehicle=vehicle_history1, information_fine=fine_history1)
transport2 = TransportAgency(agency=agency2, information_vehicle=vehicle_history2, information_fine=fine_history2)
