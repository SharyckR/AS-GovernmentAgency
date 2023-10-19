from fastapi import FastAPI, HTTPException, status
from controller.address_controller import AddressController
from controller.health_factory_controller import HealthFactoryController
from controller.legal_factory_controller import LegalFactoryController
from controller.transport_factory_controller import TransportFactoryController
from controller.mediator import *
from controller.educational_factory_controller import *
from logic.person import Person

address_controller = AddressController()
mediator_controller = Mediator()
educational_factory_controller = EducationalFactoryController()
health_factory_controller = HealthFactoryController()
legal_factory_controller = LegalFactoryController()
transport_factory_controller = TransportFactoryController()
app = FastAPI()


@app.get('/')  # Tested
async def root():
    return {'Message': 'Welcome to our FastAPI'}

# Services by person


@app.get('/persons')  # Tested
async def get_person():
    try:
        data = mediator_controller.get_persons()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=str(e))
    else:
        return {'Persons:': data}


@app.get('/persons/{dni_person}')  # Tested
async def get_person_by_id(dni_person: int):
    try:
        person_info = get_person_info(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return person_info


@app.post('/persons', status_code=status.HTTP_201_CREATED)  # Tested
async def add_person(person: Person):
    try:
        person_added = mediator_controller.add_person(person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Person added': person_added}


@app.get('/persons/educational-history/{dni_person}')  # Tested
async def get_histories_by_id(dni_person: int):
    try:
        histories = get_educational_history(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@app.get('/persons/fine-history/{dni_person}')  # Tested
async def get_histories_by_id(dni_person: int):
    try:
        histories = get_fine_history(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@app.get('/persons/vehicle-history/{dni_person}')  # Tested
async def get_histories_by_id(dni_person: int):
    try:
        histories = get_vehicle_history(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@app.get('/persons/case-history/{dni_person}')  # Tested
async def get_histories_by_id(dni_person: int):
    try:
        histories = get_case_history(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@app.get('/persons/medical-history/{dni_person}')  # Tested
async def get_histories_by_id(dni_person: int):
    try:
        histories = get_medical_history(dni_person)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return histories


@app.put('/persons/link-educational-history/{dni_person}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_education_history_to_person(dni_person: int, education_history: EducationHistory):
    try:
        educational_history = mediator_controller.link_education_history_to_person(dni_person, education_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated educational history': educational_history}


@app.put('/persons/link-fine-history/{dni_person}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_fine_history_to_person(dni_person: int, fine_history: FineHistory):
    try:
        fine_history = mediator_controller.link_fine_history_to_person(dni_person, fine_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated fine history': fine_history}


@app.put('/persons/link-vehicle-history/{dni_person}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_vehicle_history_to_person(dni_person: int, vehicle_history: VehicleHistory):
    try:
        vehicle_history = mediator_controller.link_vehicle_history_to_person(dni_person, vehicle_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated vehicle history': vehicle_history}


@app.put('/persons/link-case-history/{dni_person}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_case_history_to_person(dni_person: int, case_history: CaseHistory):
    try:
        case_history = mediator_controller.link_case_history_to_person(dni_person, case_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated case history': case_history}


@app.put('/persons/link-medical-history/{dni_person}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_medical_history_to_person(dni_person: int, medical_history: MedicalHistory):
    try:
        medical_history = mediator_controller.link_medical_history_to_person(dni_person, medical_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Updated medical history': medical_history}


# Services by agency


@app.get('/agencies/educational-agencies')  # Tested
async def get_educational_agencies():
    try:
        agencies = educational_factory_controller.get_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational Agencies': agencies}


@app.get('/agencies/legal-agencies')  # Tested
async def get_legal_agencies():
    try:
        agencies = legal_factory_controller.get_legal_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Legal Agencies': agencies}


@app.get('/agencies/transport-agencies')  # Tested
async def get_transport_agencies():
    try:
        agencies = transport_factory_controller.get_transport_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Transport Agencies': agencies}


@app.get('/agencies/health-agencies')  # Tested
async def get_health_agencies():
    try:
        agencies = health_factory_controller.get_agencies()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Health Agencies': agencies}


@app.post('/agencies/educational-agencies', status_code=status.HTTP_201_CREATED)  # Tested
async def create_educational_agency(agency: AgencyFactory, achievements: List[str]):
    try:
        ed_agency = educational_factory_controller.add_agency(agency, achievements)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Education Agency': ed_agency}


@app.post('/agencies/legal-agencies', status_code=status.HTTP_201_CREATED)  # Tested
async def create_legal_agency(agency: AgencyFactory):
    try:
        legal_agency = legal_factory_controller.add_legal_agency(agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Legal Agency': legal_agency}


@app.post('/agencies/transport-agencies', status_code=status.HTTP_201_CREATED)  # Tested
async def create_transport_agency(agency: AgencyFactory):
    try:
        transport_agency = transport_factory_controller.add_transport_agency(agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Transport Agency': transport_agency}


@app.post('/agencies/health-agencies', status_code=status.HTTP_201_CREATED)  # Tested
async def create_health_agency(agency: AgencyFactory):
    try:
        health_agency = health_factory_controller.add_agency(agency)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Health Agency': health_agency}


@app.put('/agencies/educational-agencies/{id_entity}', status_code=status.HTTP_200_OK)  # Tested
async def update_educational_agency(id_entity: int, agency: AgencyFactory, academic_achievements: List[str]):
    try:
        agency, academic_achievements = educational_factory_controller.update_agency(id_entity, agency,
                                                                                     academic_achievements)
    except Exception as e:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency,
                'Academic Achievements': academic_achievements}


@app.put('/agencies/update-legal-agencies/{id_entity}', status_code=status.HTTP_200_OK)  # Tested
async def update_legal_agency(id_entity: int, agency: AgencyFactory):
    try:
        agency = legal_factory_controller.update_legal_agency(id_entity, agency)
    except Exception as e:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency}


@app.put('/agencies/update-transport-agencies/{id_entity}', status_code=status.HTTP_200_OK)  # Tested
async def update_transport_agency(id_entity: int, agency: AgencyFactory):
    try:
        agency = transport_factory_controller.update_transport_agency(id_entity, agency)
    except Exception as e:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency}


@app.put('/agencies/health-agencies/{id_entity}', status_code=status.HTTP_200_OK)  # Tested
async def update_health_agency(id_entity: int, agency: AgencyFactory):
    try:
        agency = health_factory_controller.update_agency(id_entity, agency)
    except Exception as e:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Agency': agency}


@app.put('/agencies/link-educational-agencies/{id_entity}', status_code=status.HTTP_201_CREATED)
async def link_educational_history(education_history: EducationHistory, id_entity: int):
    try:
        ed_history = educational_factory_controller.link_agency_with_history(id_entity, education_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational History': ed_history}


@app.put('/agencies/link-legal-agencies/{id_entity}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_case_history(case_history: CaseHistory, id_entity: int):
    try:
        legal_history = legal_factory_controller.link_legal_agency_with_history(id_entity, case_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Case History': legal_history}


@app.put('/agencies/link-transport-fine-agencies/{id_entity}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_fine_history(fine_history: FineHistory, id_entity: int):
    try:
        transport_history = transport_factory_controller.link_transport_agency_with_fine_history(id_entity,
                                                                                                 fine_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Fine History': transport_history}


@app.put('/agencies/link-transport-vehicle-agencies/{id_entity}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_vehicle_history(vehicle_history: VehicleHistory, id_entity: int):
    try:
        transport_history = transport_factory_controller.link_transport_agency_with_vehicle_history(id_entity,
                                                                                                    vehicle_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Vehicle History': transport_history}


@app.put('agencies/link-health-agencies/{id_entity}', status_code=status.HTTP_201_CREATED)  # Tested
async def link_health_history(history: MedicalHistory, id_entity):
    try:
        medical_history = health_factory_controller.link_agency_with_history(id_entity, history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Health History': medical_history}


# Services by history


@app.get('/histories/educational-histories')  # Tested
async def get_educational_histories():
    try:
        histories = educational_factory_controller.get_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Educational Histories': histories}


@app.get('/histories/case-histories')  # Tested
async def get_case_histories():
    try:
        histories = legal_factory_controller.get_case_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Case Histories': histories}


@app.get('/histories/fine-histories')  # Tested
async def get_fine_histories():
    try:
        histories = transport_factory_controller.get_fine_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Fine Histories': histories}


@app.get('/histories/vehicle-histories')  # Tested
async def get_vehicle_histories():
    try:
        histories = transport_factory_controller.get_vehicle_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Vehicle Histories': histories}


@app.get('/histories/health-histories')  # Tested
async def get_medical_histories():
    try:
        histories = health_factory_controller.get_histories()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    else:
        return {'Medical Histories': histories}


@app.post('/histories/new-educational-histories', status_code=status.HTTP_201_CREATED)  # Tested
async def create_medical_history(
        dni_person: int, education: Optional[str], name_institution: Optional[str], location: Optional[Address],
        title_obtained: Optional[str], day: Optional[int], month: Optional[int], year: Optional[int]):
    try:
        educational_history = educational_factory_controller.add_ed_history(
            dni_person, education, name_institution, location, title_obtained, day, month, year)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Medical History': educational_history}


@app.post('/histories/new-case-histories', status_code=status.HTTP_201_CREATED)  # Tested
async def create_case_history(case_history: CaseHistory):
    try:
        legal_history = legal_factory_controller.add_case_history(case_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Case History': legal_history}


@app.post('/histories/new-fine-histories', status_code=status.HTTP_201_CREATED)  # Tested
async def create_fine_history(fine_history: FineHistory):
    try:
        transport_history = transport_factory_controller.add_fine_history(fine_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Fine History': transport_history}


@app.post('/histories/new-vehicle-histories', status_code=status.HTTP_201_CREATED)  # Tested
async def create_vehicle_history(vehicle_history: VehicleHistory):
    try:
        transport_history = transport_factory_controller.add_vehicle_history(vehicle_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Vehicle History': transport_history}


@app.post('/histories/new-medical-histories', status_code=status.HTTP_201_CREATED)  # Tested
async def create_medical_history(
        dni_person: int, type_blood: str, pathologies: str, description_treatment: str, doctor_charge: str,
        day: Optional[int], month: Optional[int], year: Optional[int]):
    try:
        medical_history = health_factory_controller.add_md_history(
            dni_person, type_blood, pathologies, description_treatment, doctor_charge, day, month, year)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    else:
        return {'Medical History': medical_history}
