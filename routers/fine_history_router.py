from typing import Dict
from fastapi import APIRouter, HTTPException, status
from logic.fine_history import FineHistory
from routers.transport_agency_router import transport_factory_controller
router = APIRouter(prefix='/histories', tags=['fine history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/fine-histories', response_model=Dict)  # Tested
async def get_fine_histories():
    try:
        histories = transport_factory_controller.get_fine_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Fine Histories': histories}


@router.post('/new-fine-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_fine_history(fine_history: FineHistory):
    try:
        transport_history = transport_factory_controller.add_fine_history(fine_history.to_dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Fine History': transport_history}
