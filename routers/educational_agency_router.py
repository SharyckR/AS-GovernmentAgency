from fastapi import APIRouter, HTTPException, status, Depends
from typing import Union, Dict, List
from typing_extensions import Annotated
from logic.agency_factory import AgencyFactory
from controller.educational_factory_controller import EducationalFactoryController
from logic.education_history import EducationHistory
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
from routers.auth import current_user
router = APIRouter(prefix='/agencies', tags=['educational agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
educational_factory_controller = EducationalFactoryController()


@router.get('/educational-agencies', response_model=Dict)  # Tested
async def get_educational_agencies(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.type == 'Legal Entity':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agencies = educational_factory_controller.get_agencies()
        return {'Educational Agencies': agencies}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/educational-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_educational_agency(agency: AgencyFactory, educational_histories: Union[List[EducationHistory], None],
                                    user: Annotated[Union[NaturalEntity, LegalEntity],
                                    Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Educational Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        print(agency)
        ed_agency = educational_factory_controller.add_educational_agency(agency, educational_histories)
        return {'Education Agency': ed_agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put('/update-educational-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)
# Tested
async def update_educational_agency(id_entity: int, agency: AgencyFactory,
                                    user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Educational Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agency = educational_factory_controller.update_educational_agency(id_entity, agency)
        return {'Agency': agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-educational-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_educational_history(education_history: EducationHistory, id_entity: int,
                                   user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (user.type == 'Legal Entity' and user.subtype == 'Educational Agency'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        ed_history = educational_factory_controller.link_agency_with_history(id_entity, education_history)
        return {'Educational History': ed_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
