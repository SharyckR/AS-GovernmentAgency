from typing import Dict
from fastapi import APIRouter, HTTPException, status
from controller.health_factory_controller import HealthFactoryController
from logic.agency_factory import AgencyFactory
from logic.medical_history import MedicalHistory
router = APIRouter(prefix='/agencies', tags=['health agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
health_factory_controller = HealthFactoryController()


@router.get('/health-agencies', response_model=Dict)  # Tested
async def get_health_agencies():
    try:
        agencies = health_factory_controller.get_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Health Agencies': agencies}


@router.post('/health-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_health_agency(agency: AgencyFactory):
    try:
        health_agency = health_factory_controller.add_health_agency(agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Health Agency': health_agency}


@router.put('/health-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)  # Tested
async def update_health_agency(id_entity: int, agency: AgencyFactory):
    try:
        agency = health_factory_controller.update_health_agency(id_entity, agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency}


@router.put('/link-health-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_health_history(history: MedicalHistory, id_entity: int):
    try:
        medical_history = health_factory_controller.link_agency_with_history(id_entity, history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Health History': medical_history}
