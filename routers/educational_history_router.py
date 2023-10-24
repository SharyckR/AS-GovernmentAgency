from typing import Dict
from fastapi import APIRouter, HTTPException, status
from logic.education_history import EducationHistory
from routers.educational_agency_router import educational_factory_controller
router = APIRouter(prefix='/histories', tags=['educational history'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.get('/educational-histories', response_model=Dict)  # Tested
async def get_educational_histories():
    try:
        histories = educational_factory_controller.get_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational Histories': histories}


@router.post('/new-educational-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_educational_history(education_history: EducationHistory):
    try:
        educational_history = educational_factory_controller.add_ed_history(education_history.to_dict())
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Educational History': educational_history}
