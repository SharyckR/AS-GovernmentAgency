from typing import Union, Dict, List

import identity
from fastapi import APIRouter, HTTPException, status, Depends
from identity import web
from controller.educational_factory_controller import EducationalFactoryController
from logic.agency_factory import AgencyFactory
from logic.education_history import EducationHistory
from routers.auth import get_auth
from routers.legal_agency_router import legal_factory_controller

router = APIRouter(prefix='/agencies', tags=['educational agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
educational_factory_controller = EducationalFactoryController()


@router.get('/educational-agencies', response_model=Dict)  # Tested
async def get_educational_agencies(auth: identity.web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user or user.subtype != 'Legal Agency':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = legal_factory_controller.get_case_histories()  # Assuming this function exists
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    return {'Case Histories': histories}


@router.post('/educational-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_educational_agency(agency: AgencyFactory,
                                    educational_histories: Union[List[EducationHistory], None],
                                    auth: identity.web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        ed_agency = educational_factory_controller.add_educational_agency(agency=agency,
                                                                          educational_histories=educational_histories)
        return {'Education Agency': ed_agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put('/update-educational-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)
# Tested
async def update_educational_agency(id_entity: int, agency: AgencyFactory,
                                    auth: identity.web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
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
                                   auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        ed_history = educational_factory_controller.link_agency_with_history(id_entity, education_history)
        return {'Educational History': ed_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
