from typing import Dict, Union, List
from typing_extensions import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from controller.health_factory_controller import HealthFactoryController
from logic.agency_factory import AgencyFactory
from logic.legal_entity import LegalEntity
from logic.medical_history import MedicalHistory
from logic.natural_entity import NaturalEntity
from routers.auth import current_user
router = APIRouter(prefix='/agencies', tags=['health agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
health_factory_controller = HealthFactoryController()


@router.get('/health-agencies', response_model=Dict)  # Tested
async def get_health_agencies(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.type == 'Legal Entity':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agencies = health_factory_controller.get_agencies()
        return {'Health Agencies': agencies}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/health-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_health_agency(agency: AgencyFactory, medical_histories: Union[List[MedicalHistory], None],
                               user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.type == 'Legal Entity':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        health_agency = health_factory_controller.add_health_agency(agency, medical_histories)
        return {'Health Agency': health_agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put('/health-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)  # Tested
async def update_health_agency(id_entity: int, agency: AgencyFactory,
                               user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.type == 'Legal Entity':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agency = health_factory_controller.update_health_agency(id_entity, agency)
        return {'Agency': agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-health-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_health_history(history: MedicalHistory, id_entity: int,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Health Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        medical_history = health_factory_controller.link_agency_with_history(id_entity, history)
        return {'Health History': medical_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
