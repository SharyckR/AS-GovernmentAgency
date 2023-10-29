from os import getenv
from typing import List
from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.health_factory import HealthFactory
from logic.medical_history import MedicalHistory

load_dotenv()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
MY_DB = MY_CLIENT['Entity']
HISTORIES = MY_CLIENT['Histories']
HEALTH_AGENCY_DB = MY_DB['Health Agency']
HEALTH_HISTORY_DB = HISTORIES['Medical History']


class HealthFactoryController:
    def __init__(self):
        self._health_factory: HealthFactory = HealthFactory()
        self._health_agencies: List = []
        self._health_histories: List = []
        self.load_data_db()

    def load_data_db(self):
        self._health_agencies = []
        self._health_histories = []
        for health_agency in HEALTH_AGENCY_DB.find():
            if '_id' in health_agency:
                del health_agency['_id']
            self._health_agencies.append(health_agency)
        for health_history in HEALTH_HISTORY_DB.find():
            if '_id' in health_history:
                del health_history['_id']
            self._health_histories.append(health_history)

    def add_health_agency(self, agency: AgencyFactory = AgencyFactory()):
        self.load_data_db()
        health_agency = self._health_factory.create_agency(agency=agency)
        if not any(ha[f'{list(ha.keys())[0]}']['agency']['id_entity'] == agency.id_entity
                   for ha in self._health_agencies):
            self._health_agencies.append(health_agency.to_dict())
            print(f'{health_agency.__class__.__name__} Added\n')
            HEALTH_AGENCY_DB.insert_one(health_agency.to_dict())
            return health_agency.to_dict()
        raise Exception(f'Agency with ID ENTITY: {agency.id_entity} already exist')

    def update_health_agency(self, id_entity, agency: AgencyFactory = AgencyFactory()):
        self.load_data_db()
        for ha in self._health_agencies:
            if ha[f'{list(ha.keys())[0]}']['agency']['id_entity'] == id_entity:
                update_operation = UpdateOne({f"{id_entity}.agency.id_entity": agency.id_entity},
                                             {"$set": {f"{id_entity}.agency": agency.to_dict()}})
                HEALTH_AGENCY_DB.bulk_write([update_operation])
                ha['Agency'] = agency.to_dict()
                print(f'Agency with ID Entity: {agency.id_entity} updated')
                return agency.to_dict()
        raise Exception(f'Does n\'t exist an agency with ID Entity : {id_entity}')

    def add_md_history(self, medical_history: dict):
        self.load_data_db()
        if not any(eh['id_history'] == medical_history["id_history"] for eh in self._health_histories):
            self._health_histories.append(medical_history)
            print(f'{medical_history.__class__.__name__} added\n')
            HEALTH_HISTORY_DB.insert_one(medical_history)
            if '_id' in medical_history:
                del medical_history['_id']
            return medical_history
        else:
            raise Exception(f'Medical History with ID HISTORY: {medical_history["id_history"]} already exist')

    def link_agency_with_history(self, id_health_agency: int,
                                 health_history: MedicalHistory = MedicalHistory()):
        self.load_data_db()
        health_history_dict = health_history.to_dict()
        for ha in self._health_agencies:
            if ha[f'{list(ha.keys())[0]}']['agency']['id_entity'] == id_health_agency:
                update_operation = UpdateOne(
                    {f"{id_health_agency}.agency.id_entity": id_health_agency},
                    {"$set": {f"{id_health_agency}.medical_history": health_history_dict}}
                )
                ha['medical_history'] = health_history_dict
                HEALTH_AGENCY_DB.bulk_write([update_operation])
                print(f'Linked {health_history.__class__.__name__} with {id_health_agency} '
                      f'of Health Agency')
                if '_id' in health_history_dict:
                    del health_history_dict['_id']
                return health_history_dict
        raise Exception(f'ID Entity: {id_health_agency} not found.')

    def get_agencies(self):
        self.load_data_db()
        if len(self._health_agencies) == 0:
            raise Exception('No data yet')
        return self._health_agencies

    def get_histories(self):
        self.load_data_db()
        if len(self._health_histories) == 0:
            raise Exception('No data yet')
        return self._health_histories
