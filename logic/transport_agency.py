from logic.agency_factory import AgencyFactory, agency1, agency2
from logic.fine_history import FineHistory, fine_history1, fine_history2
from logic.vehicle_history import VehicleHistory, vehicle_history1, vehicle_history2


class TransportAgency(AgencyFactory):
    """
    Represents a transport agency.

    Attributes:
        agency (object): The associated agency factory.
        licence (bool): Indicates if the agency has a license.
        type_licence (str): The type of license held by the agency.
        information_vehicle (object): Information about vehicles.
        information_fine (object): Information about fines.

    Methods:
        __str__(): Returns a formatted string with transport agency information.
        __eq__(other): Compares if two instances of TransportAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    licence: str = 'Yes or No'
    type_licence: str = 'A1, A2, B1, B2, B3, C1, C2, C3'
    information_vehicle: VehicleHistory = VehicleHistory()
    information_fine: FineHistory = FineHistory()

    def to_dict(self):
        return {
            "Agency": self.agency.to_dict(),
            "Licence": self.licence,
            "Type of licence": self.type_licence,
            "Information vehicle": self.information_vehicle.to_dict(),
            "Information fine": self.information_fine.to_dict()
        }

    def __str__(self):
        """
        Returns a formatted string with transport agency information.

        :returns: string transport agency
        :rtype: str
        """
        return 'Agency: {0}, Licence: {1}, Type of licence: {2}, Information vehicle: {3}, ' \
               'Information fine: {4}'.format(self.agency.__str__(), self.licence, self.type_licence,
                                              self.information_vehicle.__str__(), self.information_fine)

    def __eq__(self, other):
        """
        Compares if two instances of TransportAgency are equal.

        Args:
            other (TransportAgency): The other instance to compare.

        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, TransportAgency):
            return (self.agency.__eq__(other.agency) and self.licence == other.licence and
                    self.type_licence == other.type_licence and
                    self.information_vehicle.__eq__(other.information_vehicle) and
                    self.information_fine.__eq__(other.information_fine))


if __name__ == '__main__':
    transport1 = TransportAgency(agency=agency1, licence='Yes', type_licence='A1',
                                 information_vehicle=vehicle_history1, information_fine=fine_history1)
    transport2 = TransportAgency(agency=agency2, licence='No', type_licence='B2',
                                 information_vehicle=vehicle_history2, information_fine=fine_history2)

    print(f"Transport Agency 1 Information \n {transport1}")
    print(f"Transport Agency 2 Information \n {transport2}")

    are_equal_transport_agency = transport1.__eq__(transport2)
    print(f"Are equals ? \n {are_equal_transport_agency} \n\n")

transport1 = TransportAgency(agency=agency1, licence='Yes', type_licence='A1',
                             information_vehicle=vehicle_history1, information_fine=fine_history1)
transport2 = TransportAgency(agency=agency2, licence='No', type_licence='B2',
                             information_vehicle=vehicle_history2, information_fine=fine_history2)
