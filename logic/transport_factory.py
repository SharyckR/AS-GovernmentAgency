from typing import Tuple, Optional

from logic.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency import Agency
from logic.fine_history import FineHistory
from logic.transport_agency import TransportAgency
from logic.vehicle_history import VehicleHistory


class TransportFactory(AbstractFactory):
    """
    Concrete factory for creating transport agency and history objects.

    Attributes:
        None

    Methods:
        create_agency(agency: Agency = None, licence: bool = None, type_licence: str = None,
                      information_vehicle: VehicleHistory = None, information_fine: FineHistory = None
                      ) -> AbstractAgency:
            Create an instance of a TransportAgency.

        create_history(dni_person: int = None, licence: str = None, type_licence: Optional[str] = None,
                       vehicle: str = None, type_vehicle: Optional[str] = "Car or Motorcycle",
                       description_vehicle: Optional[str] = None, plate_vehicle: Optional[str] = None,
                       mediator: object = None) -> Tuple[AbstractHistory, AbstractHistory]:
            Create an instance of VehicleHistory and FineHistory as a tuple.
    """
    def create_agency(self, agency: Agency = None, licence: str = None, type_licence: str = None,
                      information_vehicle: VehicleHistory = None, information_fine: FineHistory = None
                      ) -> AbstractAgency:
        """
        Create an instance of a TransportAgency.

        Args:
            agency (Agency): The agency associated with the transport agency.
            licence (bool): Whether a licence is held or not.
            type_licence (str): Type of licence.
            information_vehicle (VehicleHistory): Information about the vehicle history.
            information_fine (FineHistory): Information about fines.

        Returns:
            AbstractAgency: An instance of TransportAgency or its subclass.
        """
        return TransportAgency(agency=agency, licence=licence, type_licence=type_licence,
                               information_vehicle=information_vehicle, information_fine=information_fine)

    def create_history(self, dni_person: int = None, licence: Optional[str] = None, type_licence: Optional[str] = None,
                       vehicle: Optional[str] = None, type_vehicle: Optional[str] = None,
                       description_vehicle: Optional[str] = None, plate_vehicle: Optional[str] = None,
                       mediator: object = None, fine: Optional[str] = None, type_fine: Optional[str] = None,
                       description_fine: Optional[str] = None, paid: Optional[str] = None,
                       ) -> Tuple[AbstractHistory, AbstractHistory]:
        """
        Create an instance of VehicleHistory and FineHistory as a tuple.

        Args:
            dni_person (int): The DNI of the person with the transport history.
            licence (str): Licence information.
            type_licence (str): Type of licence.
            vehicle (str): Vehicle information.
            type_vehicle (str): Type of vehicle (default is "Car or Motorcycle").
            description_vehicle (str): Description of the vehicle.
            plate_vehicle (str): Vehicle plate information.
            mediator (object): Mediator object.

        Returns:
            Tuple[AbstractHistory, AbstractHistory]: A tuple containing instances of VehicleHistory and FineHistory.
            :param fine:
            :param type_fine:
            :param type_licence:
            :param licence:
            :param dni_person:
            :param plate_vehicle:
            :param paid:
            :param type_vehicle:
            :param vehicle:
            :param description_vehicle:
            :param mediator:
            :param description_fine:
        """
        vehicle_history = VehicleHistory(dni_person=dni_person, licence=licence, type_licence=type_licence,
                                         vehicle=vehicle, type_vehicle=type_vehicle,
                                         description_vehicle=description_vehicle, plate_vehicle=plate_vehicle)
        fine_history = FineHistory(dni_person=dni_person, fine=fine, type_fine=type_fine,
                                   description_fine=description_fine, paid=paid)
        return vehicle_history, fine_history
