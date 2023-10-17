from fastapi import FastAPI, HTTPException, status
from controller.address_controller import AddressController
from controller.mediator import *
from controller.educational_factory_controller import *
from logic.person import Person

address_controller = AddressController()
mediator_controller = Mediator()
educational_factory_controller = EducationalFactoryController()

app = FastAPI()


@app.get('/')
async def root():
    return {'Message': 'Welcome to our FastAPI'}


@app.get('/persons')
async def get_person():
    try:
        data = mediator_controller.get_persons()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=str(e))
    else:
        return {'Persons:': data}


@app.get('/persons/{dni_person}')
async def get_person(dni_person: int):
    try:
        person_info = get_person_info(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return person_info


@app.post('/persons', status_code=status.HTTP_201_CREATED)
async def add_person(person: Person):
    try:
        person_added = mediator_controller.add_person(person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        if '_id' in person_added:
            del person_added['_id']
        return {'Person added': person_added}


@app.get('/persons/educational-history/{dni_person}')
async def get_histories(dni_person: int):
    try:
        histories = get_educational_history(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@app.get('/agencies')
async def get_educational_agencies():
    try:
        agencies = educational_factory_controller.get_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational Agencies': agencies}


@app.put('/person/educational-history/{dni_person}', status_code=status.HTTP_201_CREATED)
async def link_education_history_to_person(dni_person: int, education_history: EducationHistory):
    try:
        educational_history = mediator_controller.link_education_history_to_person(dni_person, education_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated educational history': educational_history}


@app.post('/agencies')
async def create_educational_agency(agency: AgencyFactory, achievements: List[str]):
    try:
        ed_agency = educational_factory_controller.add_agency(agency, achievements)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Education History': ed_agency}


@app.put('/agencies/{id}', status_code=status.HTTP_201_CREATED)
async def link_educational_history(education_history: EducationHistory, id: int):
    try:
        ed_history = educational_factory_controller.link_agency_with_history(id, education_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational History': ed_history}
