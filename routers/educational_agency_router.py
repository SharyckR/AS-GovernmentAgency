from fastapi import APIRouter, HTTPException, status
from typing import List, Union, Dict
from logic.agency_factory import AgencyFactory
from controller.educational_factory_controller import EducationalFactoryController
from logic.education_history import EducationHistory
router = APIRouter(prefix='/agencies', tags=['educational agency'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
educational_factory_controller = EducationalFactoryController()


@router.get('/educational-agencies', response_model=Dict)  # Tested
async def get_educational_agencies():
    try:
        agencies = educational_factory_controller.get_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational Agencies': agencies}


@router.post('/educational-agencies', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_educational_agency(agency: AgencyFactory, academic_achievements: List[str]):
    try:
        ed_agency = educational_factory_controller.add_educational_agency(agency, academic_achievements)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Education Agency': ed_agency}


@router.put('/update-educational-agencies/{id_entity}', status_code=status.HTTP_200_OK, response_model=Dict)
# Tested
async def update_educational_agency(id_entity: int, agency: AgencyFactory,
                                    academic_achievements: Union[List[str], None]):
    try:
        agency, academic_achievements = educational_factory_controller.update_educational_agency(
            id_entity, agency, academic_achievements)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency, 'Academic Achievements': academic_achievements}


@router.put('/link-educational-agencies/{id_entity}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_educational_history(education_history: EducationHistory, id_entity: int):
    try:
        ed_history = educational_factory_controller.link_agency_with_history(id_entity, education_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational History': ed_history}
