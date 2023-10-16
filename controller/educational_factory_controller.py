import json
from typing import List, Optional
import pymongo

from logic.address import Address
from logic.agency_factory import AgencyFactory
from logic.education_history import EducationHistory
from logic.educational_agency import EducationalAgency
from logic.educational_factory import EducationalFactory

my_client = pymongo.MongoClient('mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk'
                                '4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g==@as-database.mongo.cosmos.azure.com:10255'
                                '/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@as-'
                                'database@')

my_db = my_client['Entity']
educational_agency_db = my_db['Educational Agency']


class EducationalFactoryController:
    def __init__(self):
        self.__educational_factory: EducationalFactory = EducationalFactory()
        self.__educational_agencies: List = []
        self.__education_history: List = []
        self.load_data()

    def load_data(self):
        try:
            with open("../data/educational_factory.json", "r") as json_file:
                data = json.load(json_file)
                self.__educational_agencies = data.get("educational_agencies", [])
                self.__education_history = data.get("educational_histories", [])
                print('Data loaded')
                print('Data : ', self.__educational_agencies)
                json_file.close()
        except FileNotFoundError:
            print('file empty')
            self.__educational_factory: EducationalFactory = EducationalFactory()
            self.__educational_agencies: List = []
            self.__education_history: List = []
        except json.decoder.JSONDecodeError:
            with open("../data/educational_factory.json", "w") as json_file:
                json.dump('{}', json_file, indent=4)
                json_file.close()

    def save_data(self):
        data = {
            'educational_agencies': self.__educational_agencies
        }
        with open('../data/educational_factory.json', 'w') as file:
            json.dump(data, file, indent=4)
            file.close()

    def add_agency(self, agency: AgencyFactory = AgencyFactory(),
                   academic_achievements: List[str] = None):
        print(self.__educational_agencies)
        if academic_achievements is None:
            academic_achievements = []
        educational_agency = self.__educational_factory.create_agency(agency=agency,
                                                                      academic_achievements=academic_achievements)
        educational_agency_dict = educational_agency.to_dict()
        if not any(ea['Agency']['ID Entity'] == agency.id_entity
                   for ea in self.__educational_agencies):
            self.__educational_agencies.append(educational_agency_dict)
            print(f'{educational_agency.__class__.__name__} Added\n')
            self.save_data()
            return educational_agency_dict
        else:
            print(f'Agency with ID ENTITY: {agency.id_entity} already exist')

    def add_ed_history(self, dni_person: int, education: Optional[str], name_institution: Optional[str],
                       location: Optional[Address], title_obtained: Optional[str], day: Optional[int],
                       month: Optional[int], year: Optional[int]):
        educational_history = self.__educational_factory.create_history(dni_person=dni_person, education=education,
                                                                        name_institution=name_institution,
                                                                        location=location,
                                                                        title_obtained=title_obtained,
                                                                        day=day, month=month, year=year
                                                                        )
        educational_history_dict = educational_history
        if not any(eh['ID Person'] == educational_history.dni_person for eh in self.__education_history):
            self.__education_history.append(educational_history_dict)
            print(f'{educational_history.__class__.__name__} added\n')
            self.save_data()
            return educational_history_dict
        else:
            print(f'Educational History with ID HISTORY: {educational_history.dni_person} already exist')

    def link_agency_with_history(self, education_history: EducationHistory = EducationHistory(),
                                 educational_agency: EducationalAgency = EducationalAgency()):
        for ea in self.__educational_agencies:
            if ea['Agency']['ID Entity'] == educational_agency.id_entity:
                ea['Education History'] = education_history.to_dict()
                self.save_data()
                print(f'Linked {education_history.__class__.__name__} with {educational_agency.__class__.__name__}')
                return
            else:
                print(f'ID Entity: {educational_agency.id_entity} does not exist')

    def get_agencies(self):
        print(self.__educational_agencies)
        return self.__educational_agencies
                