from typing import Dict, Union
from fastapi import APIRouter, HTTPException, status, Depends
from typing_extensions import Annotated
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
from logic.vehicle_history import VehicleHistory
from middlewares.security import current_user
from routers.transport_agency_router import transport_factory_controller
router = APIRouter(prefix='/histories', tags=['vehicle history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/vehicle-histories', response_model=Dict)  # Tested
async def get_vehicle_histories(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Transport Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = transport_factory_controller.get_vehicle_histories()
        return {'Vehicle Histories': histories}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/new-vehicle-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_vehicle_history(vehicle_history: VehicleHistory,
                                 user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Transport Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        transport_history = transport_factory_controller.add_vehicle_history(vehicle_history.to_dict())
        return {'Vehicle History': transport_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
