from os import getenv
from typing import List
from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.legal_factory import LegalFactory
from logic.case_history import CaseHistory

load_dotenv()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
MY_DB = MY_CLIENT["Entity"]
LEGAL_AGENCY = MY_DB["Legal Agency"]
HISTORIES = MY_CLIENT["Histories"]
COL_CASE_HISTORY = HISTORIES["Case History"]


class LegalFactoryController:
    def __init__(self):
        self._legal_factory: LegalFactory = LegalFactory()
        self._legal_agencies: List = []
        self._case_histories: List = []
        self.load_data()

    def load_data(self):
        for legal_agency in LEGAL_AGENCY.find():
            if "_id" in legal_agency:
                del legal_agency["_id"]
            self._legal_agencies.append(legal_agency)
        for case_history in COL_CASE_HISTORY.find():
            if "_id" in case_history:
                del case_history["_id"]
            self._case_histories.append(case_history)

    def add_legal_agency(self, agency: AgencyFactory = AgencyFactory()):
        self.load_data()
        legal_agency = self._legal_factory.create_agency(agency=agency)
        dict_legal_agency = legal_agency.to_dict()
        if not any(le[f"{list(le.keys())[0]}"]["agency"]["id_entity"] == agency.id_entity for le in
                   self._legal_agencies):
            self._legal_agencies.append(dict_legal_agency)
            print(f"{legal_agency.__class__.__name__} Added\n")
            LEGAL_AGENCY.insert_one(dict_legal_agency)
            return dict_legal_agency
        raise Exception(f"Agency with ID ENTITY: {agency.id_entity} already exist")

    def update_legal_agency(self, id_entity, agency):
        self.load_data()
        dict_agency = agency.to_dict()
        for le in self._legal_agencies:
            if le[f"{list(le.keys())[0]}"]["agency"]["id_entity"] == id_entity:
                update_operation = UpdateOne({f"{id_entity}.agency.id_entity": agency.id_entity},
                                             {"$set": {f"{id_entity}.agency": dict_agency}})
                LEGAL_AGENCY.bulk_write([update_operation])
                le["Agency"] = dict_agency
                print(f"Agency with ID Entity: {agency.id_entity} updated")
                return dict_agency
        raise Exception(f"Does not exist an agency with ID Entity : {id_entity}")

    def add_case_history(self, case_history: dict):
        self.load_data()
        if not any(ca["id_history"] == case_history["id_history"] for ca in self._case_histories):
            self._case_histories.append(case_history)
            print(f"{case_history.__class__.__name__} added\n")
            COL_CASE_HISTORY.insert_one(case_history)
            if "_id" in case_history:
                del case_history["_id"]
            return case_history
        else:
            raise Exception(f"Case History with ID HISTORY: {case_history["id_history"]} already exist")

    def link_legal_agency_with_history(self, id_legal_agency: int, case_history: CaseHistory = CaseHistory()):
        self.load_data()
        dict_case_history = case_history.to_dict()
        for le in self._legal_agencies:
            if le[f"{list(le.keys())[0]}"]["agency"]["id_entity"] == id_legal_agency:
                update_operation = UpdateOne(
                    {f"{id_legal_agency}.agency.id_entity": id_legal_agency},
                    {"$set": {f"{id_legal_agency}.case_history": dict_case_history}})
                le[f"{id_legal_agency}"]["case_history"] = dict_case_history
                LEGAL_AGENCY.bulk_write([update_operation])
                print(f"Linked {case_history.__class__.__name__} with {id_legal_agency} of Legal Agency")
                return dict_case_history
        raise Exception(f"ID Entity: {id_legal_agency} not found.")

    def get_legal_agencies(self):
        self.load_data()
        if len(self._legal_agencies) == 0:
            raise Exception("No data yet")
        return self._legal_agencies

    def get_case_histories(self):
        self.load_data()
        if len(self._case_histories) == 0:
            raise Exception("No data yet")
        return self._case_histories
