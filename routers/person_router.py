from typing import Dict, Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from controller.mediator import *
from logic.case_history import CaseHistory
from logic.medical_history import MedicalHistory
from logic.person import Person
from logic.vehicle_history import VehicleHistory
from routers.auth import current_user, User

router = APIRouter(prefix='/persons', tags=['person'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
mediator_controller = Mediator()


@router.get('', response_model=Dict)  # Tested
async def get_person():
    try:
        persons = mediator_controller.get_persons()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=str(e))
    else:
        return {'Persons:': persons}


@router.get('/{dni_person}', response_model=Dict)  # Tested
async def get_person_by_id(user: Annotated[User, Depends(current_user)]):
    try:
        person_info = get_person_info(user.username)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return person_info


@router.post('', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def add_person(person: Person):
    try:
        person_added = mediator_controller.add_person(person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Person added': person_added}


@router.get('/educational-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(user: Annotated[User, Depends(current_user)]):
    try:
        histories = get_educational_history(user.username)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@router.get('/fine-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(user: Annotated[User, Depends(current_user)]):
    try:
        histories = get_fine_history(user.username)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@router.get('/vehicle-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(user: Annotated[User, Depends(current_user)]):
    try:
        histories = get_vehicle_history(user.username)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@router.get('/case-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(user: Annotated[User, Depends(current_user)]):
    try:
        histories = get_case_history(user.username)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@router.get('/medical-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(user: Annotated[User, Depends(current_user)]):
    try:
        histories = get_medical_history(user.username)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@router.put('/link-educational-history/{dni_person}', status_code=status.HTTP_201_CREATED,
            response_model=Dict)  # Tested
async def link_education_history_to_person(dni_person: int, education_history: EducationHistory = EducationHistory()):
    try:
        educational_history = mediator_controller.link_education_history_to_person(dni_person,
                                                                                   education_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated educational history': educational_history}


@router.put('/link-fine-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_fine_history_to_person(dni_person: int, fine_history: FineHistory):
    try:
        fine_history = mediator_controller.link_fine_history_to_person(dni_person, fine_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated fine history': fine_history}


@router.put('/link-vehicle-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_vehicle_history_to_person(dni_person: int, vehicle_history: VehicleHistory):
    try:
        vehicle_history = mediator_controller.link_vehicle_history_to_person(dni_person, vehicle_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated vehicle history': vehicle_history}


@router.put('/link-case-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_case_history_to_person(dni_person: int, case_history: CaseHistory):
    try:
        case_history = mediator_controller.link_case_history_to_person(dni_person, case_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated case history': case_history}


@router.put('/link-medical-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_medical_history_to_person(dni_person: int, medical_history: MedicalHistory):
    try:
        medical_history = mediator_controller.link_medical_history_to_person(dni_person, medical_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated medical history': medical_history}
