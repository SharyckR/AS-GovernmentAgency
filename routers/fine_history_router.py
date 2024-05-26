from typing import Dict
from fastapi import APIRouter, HTTPException, status, Depends
from identity import web
from logic.fine_history import FineHistory
from routers.auth import get_auth
from routers.transport_agency_router import transport_factory_controller

router = APIRouter(prefix='/histories', tags=['fine history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/fine-histories', response_model=Dict)  # Tested
async def get_fine_histories(auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = transport_factory_controller.get_fine_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Fine Histories': histories}


@router.post('/new-fine-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_fine_history(fine_history: FineHistory,
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        if not (user.type == 'Legal Entity' and user.subtype == 'Transport Agency'):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        transport_history = transport_factory_controller.add_fine_history(fine_history.to_dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Fine History': transport_history}
