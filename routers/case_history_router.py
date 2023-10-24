from typing import Dict
from fastapi import APIRouter, HTTPException, status
from logic.case_history import CaseHistory
from routers.legal_agency_router import legal_factory_controller
router = APIRouter(prefix='/histories', tags=['case history'], responses={status.HTTP_404_NOT_FOUND: {'message':
                                                                                                            'Not found'}})


@router.get('/case-histories', response_model=Dict)  # Tested
async def get_case_histories():
    try:
        histories = legal_factory_controller.get_case_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Case Histories': histories}


@router.post('/new-case-histories', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def create_case_history(case_history: CaseHistory):
    try:
        legal_history = legal_factory_controller.add_case_history(case_history.to_dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Case History': legal_history}
    