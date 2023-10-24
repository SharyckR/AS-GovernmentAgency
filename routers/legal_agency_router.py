from typing import Dict
from fastapi import APIRouter, HTTPException, status
from controller.legal_factory_controller import LegalFactoryController
from logic.agency_factory import AgencyFactory
from logic.case_history import CaseHistory
router = APIRouter(prefix='/agencies', tags=['legal agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
legal_factory_controller = LegalFactoryController()


@router.get('/legal-agencies', response_model=Dict)  # Tested
async def get_legal_agencies():
    try:
        agencies = legal_factory_controller.get_legal_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Legal Agencies': agencies}


@router.post('/legal-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_legal_agency(agency: AgencyFactory):
    try:
        legal_agency = legal_factory_controller.add_legal_agency(agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Legal Agency': legal_agency}


@router.put('/update-legal-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)  # Tested
async def update_legal_agency(id_entity: int, agency: AgencyFactory):
    try:
        agency = legal_factory_controller.update_legal_agency(id_entity, agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency}


@router.put('/link-legal-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_case_history(case_history: CaseHistory, id_entity: int):
    try:
        legal_history = legal_factory_controller.link_legal_agency_with_history(id_entity, case_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Case History': legal_history}
