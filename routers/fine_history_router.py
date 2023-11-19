from typing import Dict, Union
from typing_extensions import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from logic.fine_history import FineHistory
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
from middlewares.security import current_user
from routers.transport_agency_router import transport_factory_controller
router = APIRouter(prefix='/histories', tags=['fine history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/fine-histories', response_model=Dict)  # Tested
async def get_fine_histories(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Transport Agency':
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
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Transport Agency':
        if not (user.type == 'Legal Entity' and user.subtype == 'Transport Agency'):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        transport_history = transport_factory_controller.add_fine_history(fine_history.to_dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Fine History': transport_history}
