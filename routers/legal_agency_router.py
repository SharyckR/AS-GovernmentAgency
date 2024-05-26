from typing import Dict, Union, List

from fastapi import APIRouter, HTTPException, status, Depends
from identity import web

from controller.legal_factory_controller import LegalFactoryController
from logic.agency_factory import AgencyFactory
from logic.case_history import CaseHistory
from routers.auth import get_auth

router = APIRouter(prefix='/agencies', tags=['legal agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
legal_factory_controller = LegalFactoryController()


@router.get('/legal-agencies', response_model=Dict)  # Tested
async def get_legal_agencies(auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agencies = legal_factory_controller.get_legal_agencies()
        return {'Legal Agencies': agencies}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('/legal-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_legal_agency(agency: AgencyFactory, case_histories: Union[List[CaseHistory], None],
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        legal_agency = legal_factory_controller.add_legal_agency(agency=agency, case_histories=case_histories)
        return {'Legal Agency': legal_agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.put('/update-legal-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)  # Tested
async def update_legal_agency(id_entity: int, agency: AgencyFactory,
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        agency = legal_factory_controller.update_legal_agency(id_entity, agency)
        return {'Agency': agency}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-legal-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_case_history(case_history: CaseHistory, id_entity: int,
                            auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        legal_history = legal_factory_controller.link_legal_agency_with_history(id_entity, case_history)
        return {'Case History': legal_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
