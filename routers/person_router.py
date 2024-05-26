from typing import Dict

from fastapi import APIRouter, HTTPException, status, Depends, Request
from identity import web

from controller.mediator import *
from logic.case_history import CaseHistory
from logic.medical_history import MedicalHistory
from logic.person import Person
from logic.vehicle_history import VehicleHistory
from routers.auth import get_auth

router = APIRouter(prefix='/persons', tags=['person'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
mediator_controller = Mediator()


@router.get('', response_model=Dict)  # Tested
async def get_person(auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        persons = mediator_controller.get_persons()
        return {'Persons': persons}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=str(e))


@router.get('/{dni_person}', response_model=Dict)  # Tested
async def get_person_by_id(dni_person: int,
                           auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        person_info = get_person_info(dni_person)
        return person_info
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post('', status_code=status.HTTP_201_CREATED, response_model=Dict)  # Tested
async def add_person(person: Person,
                     auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        person_added = mediator_controller.add_person(person)
        return {'Person added': person_added}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@router.get('/educational-history/{dni_person}', response_model=Dict)  # Tested
async def get_histories_by_id(dni_person: int,
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
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
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()
    if not user:
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
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
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
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
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
                              auth: web.Auth = Depends(get_auth)):
    user = auth.get_user()

    if not user:
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
                                           auth: web.Auth = Depends(get_auth),
                                           education_history: EducationHistory = EducationHistory()):
    user = auth.get_user()

    if not user:
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
                                      fine_history: FineHistory,
                                      auth: web.Auth = Depends(get_auth),
                                      ):
    user = auth.get_user()
    if not user:
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
                                         vehicle_history: VehicleHistory,
                                         auth: web.Auth = Depends(get_auth)
                                         ):
    user = auth.get_user()

    if not user:
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
                                      case_history: CaseHistory,
                                      auth: web.Auth = Depends(get_auth),
                                      ):
    user = auth.get_user()

    if not user:
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
                                         medical_history: MedicalHistory,
                                         auth: web.Auth = Depends(get_auth),
                                         ):
    user = auth.get_user()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='UNAUTHORIZED',
                            headers={"WWW-Authenticate": "Bearer"})
    try:
        medical_history = mediator_controller.link_medical_history_to_person(dni_person, medical_history)
        return {'Updated medical history': medical_history}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
