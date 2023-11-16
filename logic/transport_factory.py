from typing import Tuple, Union, List
from logic.abstract_agency import AbstractAgency
from logic.abstract_factory import AbstractFactory
from logic.abstract_history import AbstractHistory
from logic.agency_factory import AgencyFactory
from logic.fine_history import FineHistory
from logic.transport_agency import TransportAgency
from logic.vehicle_history import VehicleHistory


class TransportFactory(AbstractFactory):
    """
    Concrete factory for creating transport agency and history objects.
    Methods:
        create_agency(agency: AgencyFactory = AgencyFactory(),
                      vehicle_histories: List[Union[VehicleHistory, None]] = List[VehicleHistory()],
                      information_fine: List[Union[FineHistory, None]] = List[FineHistory()]) -> AbstractAgency:
            Create an instance of a TransportAgency.
        create_history(id_history: int = 1, dni_person: int = 123456789, licence: str = None, type_licence: Union[
        str] = None, vehicle: str = None, type_vehicle: Union[str] = "Car or Motorcycle", description_vehicle: Union[
        str] = None, plate_vehicle: Union[str] = None, mediator: Union[object, None] = None) -> Tuple[AbstractHistory,
        AbstractHistory]: Create an instance of VehicleHistory and FineHistory as a tuple.
    """

    def create_agency(
            self, agency: AgencyFactory = AgencyFactory(),
            vehicle_histories: List[Union[VehicleHistory, None]] = None,
            fine_histories: List[Union[FineHistory, None]] = None) -> AbstractAgency:
        """
        Create an instance of a TransportAgency.
        Args:
            agency (AgencyFactory): The agency associated with the transport agency.
            vehicle_histories (List): Information about the vehicle histories.
            fine_histories (List): Information about fines.

        Returns:
            AbstractAgency: An instance of TransportAgency or its subclass.
        """
        return TransportAgency(username=str(agency.id_entity), agency=agency, information_vehicles=vehicle_histories,
                               information_fines=fine_histories)

    def create_history(self, **kwargs) -> Tuple[AbstractHistory, AbstractHistory]:
        """
        Create an instance of VehicleHistory and FineHistory as a tuple.
        Args:
            **kwargs: Keyword arguments for vehicle information and fine information.
        Returns:
            Tuple[AbstractHistory, AbstractHistory]: A tuple containing instances of VehicleHistory and FineHistory.
        """
        vehicle_inf = kwargs.get('vehicle_inf', {})  # Extract vehicle information
        fine_inf = kwargs.get('fine_inf', {})  # Extract fine information

        vehicle_history = VehicleHistory(**vehicle_inf)
        fine_history = FineHistory(**fine_inf)
        return vehicle_history, fine_history
