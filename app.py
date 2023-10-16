from fastapi import FastAPI, HTTPException, status
from controller.address_controller import AddressController
from controller.mediator import *
from logic.person import Person


address_controller = AddressController()
mediator_controller = Mediator()
app = FastAPI()


@app.get('/')
async def root():
    return {'Message': 'Welcome to our FastAPI'}


@app.get('/persons')
async def get_address():
    data = []
    if my_col.count_documents({}) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No data yet')
    for c in my_col.find():
        if '_id' in c:
            del c['_id']
        data.append(c)
    return {'Data:': data}


@app.post('/persons', status_code=status.HTTP_201_CREATED)
async def add_person(person: Person):
    person_added = mediator_controller.add_person(person)
    if not person_added:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Person with DNI {person.dni} already exists.')
    if '_id' in person_added:
        del person_added['_id']
    return person_added
