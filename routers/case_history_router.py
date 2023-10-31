from typing import Dict, Annotated, Union
from fastapi import APIRouter, HTTPException, status, Depends
from logic.case_history import CaseHistory
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
from routers.auth import current_user
from routers.legal_agency_router import legal_factory_controller
router = APIRouter(prefix='/histories', tags=['case history'], responses={status.HTTP_404_NOT_FOUND: {'message':
                                                                                                            'Not found'}})


@router.get('/case-histories', response_model=Dict)  # Tested
async def get_case_histories(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Case Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = legal_factory_controller.get_case_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Case Histories': histories}


@router.post('/new-case-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_case_history(case_history: CaseHistory,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Case Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        legal_history = legal_factory_controller.add_case_history(case_history.to_dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Case History': legal_history}
    