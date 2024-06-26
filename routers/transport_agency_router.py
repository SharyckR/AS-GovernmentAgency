from typing import Dict, Union, List

from fastapi import APIRouter, HTTPException, status, Depends
from identity import web

from controller.transport_factory_controller import TransportFactoryController
from logic.agency_factory import AgencyFactory
from logic.fine_history import FineHistory
from logic.vehicle_history import VehicleHistory
from routers.auth import get_auth

router = APIRouter(prefix='/agencies', tags=['transport agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
transport_factory_controller = TransportFactoryController()


@router.get('/transport-agencies', response_model=Dict)  # Tested
async def get_transport_agencies(auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agencies = transport_factory_controller.get_transport_agencies()
        return {'Transport Agencies': agencies}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/transport-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_transport_agency(agency: AgencyFactory, vehicle_histories: Union[List[VehicleHistory], None],
                                  fine_histories: Union[List[FineHistory], None],
                                  auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        transport_agency = transport_factory_controller.add_transport_agency(agency=agency,
                                                                             vehicle_histories=vehicle_histories,
                                                                             fine_histories=fine_histories)
        return {'Transport Agency': transport_agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put('/update-transport-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)
# Tested
async def update_transport_agency(id_entity: int, agency: AgencyFactory,
                                  auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agency = transport_factory_controller.update_transport_agency(id_entity, agency)
        return {'Agency': agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-transport-fine-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_fine_history(fine_history: FineHistory, id_entity: int,
                            auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        transport_history = transport_factory_controller.link_transport_agency_with_fine_history(
            id_entity, fine_history)
        return {'Fine History': transport_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-transport-vehicle-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_vehicle_history(vehicle_history: VehicleHistory, id_entity: int,
                               auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        transport_history = transport_factory_controller.link_transport_agency_with_vehicle_history(
            id_entity, vehicle_history)
        return {'Vehicle History': transport_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
