from typing import Dict

from fastapi import APIRouter, HTTPException, status, Depends
from identity import web

from logic.medical_history import MedicalHistory
from routers.auth import get_auth
from routers.health_agency_router import health_factory_controller

router = APIRouter(prefix='/histories', tags=['health history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/health-histories', response_model=Dict)  # Tested
async def get_medical_histories(auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = health_factory_controller.get_histories()
        return {'Medical Histories': histories}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/new-medical-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_medical_history(medical_history: MedicalHistory,
                                 auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        medical_history = health_factory_controller.add_md_history(medical_history.to_dict())
        return {'Medical History': medical_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
