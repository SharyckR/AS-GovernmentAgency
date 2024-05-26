from typing import Dict

from fastapi import APIRouter, HTTPException, status, Depends
from identity import web

from logic.education_history import EducationHistory
from routers.auth import get_auth
from routers.educational_agency_router import educational_factory_controller

router = APIRouter(prefix='/histories', tags=['educational history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/educational-histories', response_model=Dict)  # Tested
async def get_educational_histories(auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})

    try:
        histories = educational_factory_controller.get_histories()
        return {'Educational Histories': histories}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/new-educational-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_educational_history(education_history: EducationHistory,
                                     auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        educational_history = educational_factory_controller.add_ed_history(education_history.to_dict())
        return {'Educational History': educational_history}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
