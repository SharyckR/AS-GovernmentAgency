from typing import Dict
from fastapi import APIRouter, HTTPException, status
from logic.vehicle_history import VehicleHistory
from routers.transport_agency_router import transport_factory_controller
router = APIRouter(prefix='/histories', tags=['vehicle history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/vehicle-histories', response_model=Dict)  # Tested
async def get_vehicle_histories():
    try:
        histories = transport_factory_controller.get_vehicle_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Vehicle Histories': histories}


@router.post('/new-vehicle-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_vehicle_history(vehicle_history: VehicleHistory):
    try:
        transport_history = transport_factory_controller.add_vehicle_history(vehicle_history.to_dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Vehicle History': transport_history}
