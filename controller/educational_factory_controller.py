from typing import List
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.education_history import EducationHistory
from logic.educational_factory import EducationalFactory

MY_CLIENT = MongoClient(
    'mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g'
    '==@as-database.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000'
    '&appName=@as-database@')
MY_DB = MY_CLIENT['Entity']
HISTORIES = MY_CLIENT['Histories']
EDUCATIONAL_AGENCY_DB = MY_DB['Educational Agency']
EDUCATIONAL_HISTORY_DB = HISTORIES['Educational History']


class EducationalFactoryController:
    def __init__(self):
        self._educational_factory: EducationalFactory = EducationalFactory()
        self._educational_agencies: List = []
        self._educational_histories: List = []
        self.load_data_db()

    def load_data_db(self):
        self._educational_histories = []
        self._educational_agencies = []
        for educational_agency in EDUCATIONAL_AGENCY_DB.find():
            if '_id' in educational_agency:
                del educational_agency['_id']
            self._educational_agencies.append(educational_agency)
        for educational_history in EDUCATIONAL_HISTORY_DB.find():
            if '_id' in educational_history:
                del educational_history['_id']
            self._educational_histories.append(educational_history)

    def add_educational_agency(self, agency: AgencyFactory = AgencyFactory(), academic_achievements: List[str] = None):
        self.load_data_db()
        if academic_achievements is None:
            academic_achievements = []
        educational_agency = self._educational_factory.create_agency(
            agency=agency, academic_achievements=academic_achievements)
        educational_agency.username = agency.id_entity
        if not any(ea[f'{list(ea.keys())[0]}']['agency']['id_entity'] == agency.id_entity
                   for ea in self._educational_agencies):
            self._educational_agencies.append(educational_agency.to_dict())
            print(f'{educational_agency.__class__.__name__} Added\n')
            EDUCATIONAL_AGENCY_DB.insert_one(educational_agency.to_dict())
            return educational_agency.to_dict()
        else:
            raise Exception(f'Agency with ID ENTITY: {agency.id_entity} already exist')

    def update_educational_agency(
            self, id_entity: int,  agency: AgencyFactory = AgencyFactory(), academic_achievements: List[str] = None):
        self.load_data_db()
        if academic_achievements is None:
            academic_achievements = []
        for ea in self._educational_agencies:
            if ea[f'{list(ea.keys())[0]}']['agency']['id_entity'] == id_entity:
                update_dict = {"$set": {f"{id_entity}.agency": agency.to_dict()}}
                if academic_achievements is not None and len(academic_achievements) != 0:
                    update_dict["$set"]["academic_achievements"] = academic_achievements
                    ea['academic_achievements'] = academic_achievements
                update_operation = UpdateOne({f"{id_entity}.agency.id_entity": id_entity}, update_dict)
                EDUCATIONAL_AGENCY_DB.bulk_write([update_operation])
                ea['agency'] = agency.to_dict()
                print(f'Agency with ID Entity: {agency.id_entity} updated')
                return agency.to_dict(), academic_achievements
        raise Exception(f'Does n\'t exist an agency with ID Entity : {id_entity}')

    def add_ed_history(self, educational_history: dict):
        self.load_data_db()
        if not any(eh['id_history'] == educational_history["id_history"] for eh in self._educational_histories):
            self._educational_histories.append(educational_history)
            print(f'{educational_history.__class__.__name__} added\n')
            EDUCATIONAL_HISTORY_DB.insert_one(educational_history)
            if '_id' in educational_history:
                del educational_history['_id']
            return educational_history
        else:
            raise Exception(f'Educational History with ID HISTORY: {educational_history["id_history"]} already exist')

    def link_agency_with_history(self, id_educational_agency: int,
                                 education_history: EducationHistory = EducationHistory()):
        self.load_data_db()
        for ea in self._educational_agencies:
            if ea[f'{list(ea.keys())[0]}']['agency']['id_entity'] == id_educational_agency:
                update_operation = UpdateOne(
                    {f"{id_educational_agency}.agency.id_entity": id_educational_agency},
                    {"$set": {f"{id_educational_agency}.education_history": education_history.to_dict()}})
                ea[f'{id_educational_agency}']['education_history'] = education_history.to_dict()
                EDUCATIONAL_AGENCY_DB.bulk_write([update_operation])
                print(f'Linked {education_history.__class__.__name__} with {id_educational_agency} '
                      f'of EducationalAgency')
                return education_history.to_dict()
        raise Exception(f'ID Entity: {id_educational_agency} not found.')

    def get_agencies(self):
        self.load_data_db()
        if len(self._educational_agencies) == 0:
            raise Exception('No data yet')
        return self._educational_agencies

    def get_histories(self):
        self.load_data_db()
        if len(self._educational_histories) == 0:
            raise Exception('No data yet')
        return self._educational_histories
