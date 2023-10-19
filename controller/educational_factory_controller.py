from typing import List, Optional
from pymongo import MongoClient, UpdateOne
from logic.address import Address
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
        self.__educational_factory: EducationalFactory = EducationalFactory()
        self.__educational_agencies: List = []
        self.__educational_histories: List = []
        self.load_data_db()

    def load_data_db(self):
        for educational_agency in EDUCATIONAL_AGENCY_DB.find():
            if '_id' in educational_agency:
                del educational_agency['_id']
            self.__educational_agencies.append(educational_agency)
        for educational_history in EDUCATIONAL_HISTORY_DB.find():
            if '_id' in educational_history:
                del educational_history['_id']
            self.__educational_histories.append(educational_history)

    def add_agency(self, agency: AgencyFactory = AgencyFactory(),
                   academic_achievements: List[str] = None):
        if academic_achievements is None:
            academic_achievements = []
        educational_agency = self.__educational_factory.create_agency(
            agency=agency, academic_achievements=academic_achievements)
        educational_agency_dict = educational_agency.to_dict()
        if not any(ea['Agency']['ID Entity'] == agency.id_entity
                   for ea in self.__educational_agencies):
            self.__educational_agencies.append(educational_agency_dict)
            print(f'{educational_agency.__class__.__name__} Added\n')
            EDUCATIONAL_AGENCY_DB.insert_one(educational_agency_dict)
            if '_id' in educational_agency_dict:
                del educational_agency_dict['_id']
            return educational_agency_dict
        else:
            raise Exception(f'Agency with ID ENTITY: {agency.id_entity} already exist')

    def update_agency(self, id_entity: int,  agency: AgencyFactory = AgencyFactory(),
                      academic_achievements: List[str] = None):
        if academic_achievements is None:
            academic_achievements = []
        for ea in self.__educational_agencies:
            if ea['Agency']['ID Entity'] == id_entity:
                update_operation = UpdateOne({"Agency.ID Entity": agency.id_entity},
                                             {"$set": {"Agency": agency.to_dict()}})
                if academic_achievements is not None:
                    update_operation["$set"]["Academic Achievements"] = academic_achievements
                    ea['Academic Achievements'] = academic_achievements
                EDUCATIONAL_AGENCY_DB.bulk_write([update_operation])
                ea['Agency'] = agency.to_dict()
                print(f'Agency with ID Entity: {agency.id_entity} updated')
                return agency.to_dict(), academic_achievements
        raise Exception(f'Does n\'t exist an agency with ID Entity : {id_entity}')

    def add_ed_history(self, dni_person: int, education: Optional[str], name_institution: Optional[str],
                       location: Optional[Address], title_obtained: Optional[str], day: Optional[int],
                       month: Optional[int], year: Optional[int]):
        educational_history = self.__educational_factory.create_history(
            dni_person=dni_person, education=education, name_institution=name_institution, location=location,
            title_obtained=title_obtained, day=day, month=month, year=year)
        educational_history_dict = educational_history.to_dict()
        if not any(eh['DNI Person'] == educational_history.dni_person for eh in self.__educational_histories):
            self.__educational_histories.append(educational_history_dict)
            print(f'{educational_history.__class__.__name__} added\n')
            EDUCATIONAL_HISTORY_DB.insert_one(educational_history_dict)
            return educational_history_dict
        else:
            raise Exception(f'Educational History with ID HISTORY: {educational_history.dni_person} already exist')

    def link_agency_with_history(self, id_educational_agency: int,
                                 education_history: EducationHistory = EducationHistory()):
        for ea in self.__educational_agencies:
            if ea['Agency']['ID Entity'] == id_educational_agency:
                update_operation = UpdateOne(
                    {"Agency.ID Entity": id_educational_agency},
                    {"$set": {"Education History": education_history.to_dict()}} )
                ea['Education History'] = education_history.to_dict()
                EDUCATIONAL_AGENCY_DB.bulk_write([update_operation])
                print(f'Linked {education_history.__class__.__name__} with {id_educational_agency} '
                      f'of EducationalAgency')
                return education_history.to_dict()
        raise Exception(f'ID Entity: {id_educational_agency} not found.')

    def get_agencies(self):
        if len(self.__educational_agencies) == 0:
            raise Exception('No data yet')
        return self.__educational_agencies

    def get_histories(self):
        if len(self.__educational_histories) == 0:
            raise Exception('No data yet')
        return self.__educational_histories
