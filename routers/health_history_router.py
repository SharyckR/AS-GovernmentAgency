from typing import Dict, Union
from fastapi import APIRouter, HTTPException, status, Depends
from typing_extensions import Annotated
from logic.legal_entity import LegalEntity
from logic.medical_history import MedicalHistory
from logic.natural_entity import NaturalEntity
from routers.auth import current_user
from routers.health_agency_router import health_factory_controller
router = APIRouter(prefix='/histories', tags=['health history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/health-histories', response_model=Dict)  # Tested
async def get_medical_histories(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Health Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = health_factory_controller.get_histories()
        return {'Medical Histories': histories}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/new-medical-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_medical_history(medical_history: MedicalHistory,
                                 user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Health Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        medical_history = health_factory_controller.add_md_history(medical_history.to_dict())
        return {'Medical History': medical_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
