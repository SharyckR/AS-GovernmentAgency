from typing import Dict
from typing_extensions import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from controller.mediator import *
from logic.case_history import CaseHistory
from logic.legal_entity import LegalEntity
from logic.medical_history import MedicalHistory
from logic.person import Person
from logic.vehicle_history import VehicleHistory
from middlewares.security import current_user
from logic.natural_entity import NaturalEntity
router = APIRouter(prefix='/persons', tags=['person'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
mediator_controller = Mediator()


@router.get('', response_model=Dict)  # Tested
async def get_person(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.type == 'Legal Entity':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        persons = mediator_controller.get_persons()
        return {'Persons:': persons}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=str(e))


@router.get('/{dni_person}', response_model=Dict)  # Tested
async def get_person_by_id(dni_person: int,
                           user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not (dni_person == int(user.username) or user.type == 'Legal Entity'):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        person_info = get_person_info(dni_person)
        return person_info
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def add_person(person: Person, user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.type == 'Legal Entity':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        person_added = mediator_controller.add_person(person)
        return {'Person added': person_added}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get('/educational-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(dni_person: int,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Educational Agency':
        if not dni_person == int(user.username):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = get_educational_history(dni_person)
        return histories
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/fine-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(dni_person: int,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Transport Agency':
        if not dni_person == int(user.username):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = get_fine_history(dni_person)
        return histories
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/vehicle-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(dni_person: int,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Transport Agency':
        if not dni_person == int(user.username):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = get_vehicle_history(dni_person)
        return histories
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/case-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(dni_person: int,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Legal Agency':
        if not dni_person == int(user.username):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = get_case_history(dni_person)
        return histories
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get('/medical-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(dni_person: int,
                              user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)]):
    if not user.subtype == 'Health Agency':
        if not dni_person == int(user.username):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                                headers={"WWW-Authenticate": "Bearer"})
    try:
        histories = get_medical_history(dni_person)
        return histories
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-educational-history/{dni_person}', status_code=status.HTTP_201_CREATED,
            response_model=Dict)  # Tested
async def link_education_history_to_person(dni_person: int,
                                           user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)],
                                           education_history: EducationHistory = EducationHistory()):
    if not user.subtype == 'Educational Agency':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        educational_history = mediator_controller.link_education_history_to_person(dni_person, education_history)
        return {'Updated educational history': educational_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-fine-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_fine_history_to_person(dni_person: int,
                                      user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)],
                                      fine_history: FineHistory):
    if not user.subtype == 'Transport Agency':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        fine_history = mediator_controller.link_fine_history_to_person(dni_person, fine_history)
        return {'Updated fine history': fine_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-vehicle-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_vehicle_history_to_person(dni_person: int,
                                         user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)],
                                         vehicle_history: VehicleHistory):
    if not user.subtype == 'Transport Agency':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        vehicle_history = mediator_controller.link_vehicle_history_to_person(dni_person, vehicle_history)
        return {'Updated vehicle history': vehicle_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-case-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_case_history_to_person(dni_person: int,
                                      user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)],
                                      case_history: CaseHistory):
    print(user.type)
    if not user.subtype == 'Legal Agency':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        case_history = mediator_controller.link_case_history_to_person(dni_person, case_history)
        return {'Updated case history': case_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put('/link-medical-history/{dni_person}', status_code=status.HTTP_201_CREATED, response_model=Dict)
# Tested
async def link_medical_history_to_person(dni_person: int,
                                         user: Annotated[Union[NaturalEntity, LegalEntity], Depends(current_user)],
                                         medical_history: MedicalHistory):
    if not user.subtype == 'Health Agency':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        medical_history = mediator_controller.link_medical_history_to_person(dni_person, medical_history)
        return {'Updated medical history': medical_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
