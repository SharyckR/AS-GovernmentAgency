from typing import List, Optional
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.health_factory import HealthFactory
from logic.medical_history import MedicalHistory

MY_CLIENT = MongoClient(
    'mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g'
    '==@as-database.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000'
    '&appName=@as-database@')
MY_DB = MY_CLIENT['Entity']
HISTORIES = MY_CLIENT['Histories']
HEALTH_AGENCY_DB = MY_DB['Health agency']
HEALTH_HISTORY_DB = HISTORIES['Medical History']


class HealthFactoryController:
    def __init__(self):
        self.__health_factory: HealthFactory = HealthFactory()
        self.__health_agencies: List = []
        self.__health_histories: List = []
        self.load_data_db()

    def load_data_db(self):
        for health_agency in HEALTH_AGENCY_DB.find():
            if '_id' in health_agency:
                del health_agency['_id']
            self.__health_agencies.append(health_agency)
        for health_history in HEALTH_HISTORY_DB.find():
            if '_id' in health_history:
                del health_history['_id']
            self.__health_histories.append(health_history)

    def add_agency(self, agency: AgencyFactory = AgencyFactory()):
        health_agency = self.__health_factory.create_agency(agency=agency)
        health_agency_dict = health_agency.to_dict()
        if not any(ha['Agency']['ID Entity'] == agency.id_entity
                   for ha in self.__health_agencies):
            self.__health_agencies.append(health_agency_dict)
            print(f'{health_agency.__class__.__name__} Added\n')
            HEALTH_AGENCY_DB.insert_one(health_agency_dict)
            if '_id' in health_agency_dict:
                del health_agency_dict['_id']
            return health_agency_dict
        else:
            raise Exception(f'Agency with ID ENTITY: {agency.id_entity} already exist')

    def update_agency(self, id_entity, agency):
        for ea in self.__health_agencies:
            if ea['Agency']['ID Entity'] == id_entity:
                update_operation = UpdateOne({"Agency.ID Entity": agency.id_entity},
                                             {"$set": {"Agency": agency.to_dict()}})
                HEALTH_AGENCY_DB.bulk_write([update_operation])
                ea['Agency'] = agency.to_dict()
                print(f'Agency with ID Entity: {agency.id_entity} updated')
                return agency.to_dict()
        raise Exception(f'Does n\'t exist an agency with ID Entity : {id_entity}')

    def add_md_history(self, dni_person: int, type_blood: str, pathologies: str,
                       description_treatment: str, doctor_charge: str, day: Optional[int],
                       month: Optional[int], year: Optional[int], mediator: object = None
                       ):
        health_history = self.__health_factory.create_history(
            dni_person=dni_person, type_blood=type_blood, pathologies=pathologies,
            description_treatment=description_treatment, doctor_charge=doctor_charge, day=day, month=month, year=year,
            mediator=mediator)
        health_history_dict = health_history.to_dict()
        if not any(eh['DNI Person'] == health_history.dni_person for eh in self.__health_histories):
            self.__health_histories.append(health_history_dict)
            print(f'{health_history.__class__.__name__} added\n')
            HEALTH_HISTORY_DB.insert_one(health_history_dict)
            return health_history_dict
        else:
            raise Exception(f'Medical History with ID HISTORY: {health_history.dni_person} already exist')

    def link_agency_with_history(self, id_health_agency: int,
                                 health_history: MedicalHistory = MedicalHistory()):
        for ha in self.__health_agencies:
            if ha['Agency']['ID Entity'] == id_health_agency:
                update_operation = UpdateOne(
                    {"Agency.ID Entity": id_health_agency},
                    {"$set": {"Medical History": health_history.to_dict()}}
                )
                ha['Medical History'] = health_history.to_dict()
                HEALTH_AGENCY_DB.bulk_write([update_operation])
                print(f'Linked {health_history.__class__.__name__} with {id_health_agency} '
                      f'of Health Agency')
                return health_history.to_dict()
        raise Exception(f'ID Entity: {id_health_agency} not found.')

    def get_agencies(self):
        if len(self.__health_agencies) == 0:
            raise Exception('No data yet')
        return self.__health_agencies

    def get_histories(self):
        if len(self.__health_histories) == 0:
            raise Exception('No data yet')
        return self.__health_histories
