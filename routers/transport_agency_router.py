from typing import Dict
from fastapi import APIRouter, HTTPException, status
from logic.agency_factory import AgencyFactory
from controller.transport_factory_controller import TransportFactoryController
from logic.fine_history import FineHistory
from logic.vehicle_history import VehicleHistory
router = APIRouter(prefix='/agencies', tags=['transport agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
transport_factory_controller = TransportFactoryController()


@router.get('/transport-agencies', response_model=Dict)  # Tested
async def get_transport_agencies():
    try:
        agencies = transport_factory_controller.get_transport_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Transport Agencies': agencies}


@router.post('/transport-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_transport_agency(agency: AgencyFactory):
    try:
        transport_agency = transport_factory_controller.add_transport_agency(agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Transport Agency': transport_agency}


@router.put('/update-transport-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)
# Tested
async def update_transport_agency(id_entity: int, agency: AgencyFactory):
    try:
        agency = transport_factory_controller.update_transport_agency(id_entity, agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency}


@router.put('/link-transport-fine-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_fine_history(fine_history: FineHistory, id_entity: int):
    try:
        transport_history = transport_factory_controller.link_transport_agency_with_fine_history(id_entity,
                                                                                                 fine_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Fine History': transport_history}


@router.put('/link-transport-vehicle-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_vehicle_history(vehicle_history: VehicleHistory, id_entity: int):
    try:
        transport_history = transport_factory_controller.link_transport_agency_with_vehicle_history(id_entity,
                                                                                                    vehicle_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Vehicle History': transport_history}
