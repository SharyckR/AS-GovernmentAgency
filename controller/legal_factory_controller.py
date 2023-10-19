from typing import List
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.legal_factory import LegalFactory
from logic.case_history import CaseHistory

MY_CLIENT = MongoClient('mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk'
                        '4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g==@as-database.mongo.cosmos.azure.com:10255'
                        '/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@as-'
                        'database@')
MY_DB = MY_CLIENT['Entity']
LEGAL_AGENCY = MY_DB['Legal Agency']
HISTORIES = MY_CLIENT['Histories']
COL_CASE_HISTORY = HISTORIES['Case History']


class LegalFactoryController:
    def __init__(self):
        self._legal_factory: LegalFactory = LegalFactory()
        self._legal_agencies: List = []
        self._case_histories: List = []
        self.load_data()

    def load_data(self):
        for legal_agency in LEGAL_AGENCY.find():
            if '_id' in legal_agency:
                del legal_agency['_id']
            self._legal_agencies.append(legal_agency)
        for case_history in COL_CASE_HISTORY.find():
            if '_id' in case_history:
                del case_history['_id']
            self._case_histories.append(case_history)

    def add_legal_agency(self, agency: AgencyFactory = AgencyFactory()):
        legal_agency = self._legal_factory.create_agency(agency=agency)
        legal_agency_dict = legal_agency.to_dict()
        if not any(ea['Agency']['ID Entity'] == agency.id_entity for ea in self._legal_agencies):
            self._legal_agencies.append(legal_agency_dict)
            print(f'{legal_agency.__class__.__name__} Added\n')
            LEGAL_AGENCY.insert_one(legal_agency_dict)
            if '_id' in legal_agency_dict:
                del legal_agency_dict['_id']
            return legal_agency_dict
        else:
            raise Exception(f'Agency with ID ENTITY: {agency.id_entity} already exists')

    def update_legal_agency(self, id_entity, agency):
        for ea in self._legal_agencies:
            if ea['Agency']['ID Entity'] == id_entity:
                update_operation = UpdateOne({"Agency.ID Entity": agency.id_entity},
                                             {"$set": {"Agency": agency.to_dict()}})
                LEGAL_AGENCY.bulk_write([update_operation])
                ea['Agency'] = agency.to_dict()
                print(f'Agency with ID Entity: {agency.id_entity} updated')
                return agency.to_dict()
        raise Exception(f'Does not exist an agency with ID Entity : {id_entity}')

    def add_case_history(self, case_history: CaseHistory = CaseHistory()):
        case_history_dict = case_history.to_dict()
        if not any(eh['DNI Person'] == case_history.dni_person for eh in self._case_histories):
            self._case_histories.append(case_history_dict)
            print(f'{case_history.__class__.__name__} added\n')
            COL_CASE_HISTORY.insert_one(case_history_dict)
            return case_history_dict
        else:
            raise Exception(f'Case History with ID HISTORY: {case_history.dni_person} already exist')

    def link_legal_agency_with_history(self, id_legal_agency: int, case_history: CaseHistory = CaseHistory()):
        case_history_dict = case_history.to_dict()
        for le in self._legal_agencies:
            if le['Agency']['ID Entity'] == id_legal_agency:
                update_operation = UpdateOne({"Agency.ID Entity": id_legal_agency},
                                             {"$set": {"Case History": case_history_dict}})
                le['Case History'] = case_history_dict
                LEGAL_AGENCY.bulk_write([update_operation])
                print(f'Linked {case_history.__class__.__name__} with {id_legal_agency} of Legal Agency')
                return case_history_dict
        raise Exception(f'ID Entity: {id_legal_agency} not found.')

    def get_legal_agencies(self):
        if len(self._legal_agencies) == 0:
            raise Exception('No data yet')
        return self._legal_agencies

    def get_case_histories(self):
        if len(self._case_histories) == 0:
            raise Exception('No data yet')
        return self._case_histories
