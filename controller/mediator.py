import pymongo
from logic.person import Person
from logic.education_history import EducationHistory
from logic.fine_history import FineHistory
from logic.case_history import CaseHistory
from logic.medical_history import MedicalHistory
from logic.vehicle_history import VehicleHistory

my_client = pymongo.MongoClient('mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk'
                                '4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g==@as-database.mongo.cosmos.azure.com:10255'
                                '/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@as-'
                                'database@')

ENTITY = my_client['Entity']
COL_PERSON = ENTITY['Person']
HISTORIES = my_client['Histories']
COL_EDUCATION_HISTORY = HISTORIES['Education History']
COL_FINE_HISTORY = HISTORIES['Fine History']
COL_VEHICLE_HISTORY = HISTORIES['Vehicle History']
COL_CASE_HISTORY = HISTORIES['Case History']
COL_MEDICAL_HISTORY = HISTORIES['Medical History']


def find_history_by_dni(history_list, dni):
    for history in history_list:
        if history.get("DNI Person") == dni:
            if history:
                return history
            else:
                return f"History for DNI {dni} not found."
    return None


# Get information for DNI

def get_person_info(dni_person: int):
    person_data = COL_PERSON.find_one({"DNI Person": dni_person})
    if person_data:
        if "_id" in person_data:
            del person_data["_id"]
        return person_data
    else:
        raise Exception(f"No person found for DNI {dni_person}")


def get_educational_history(dni_person: int):
    person_data = COL_PERSON.find_one({"DNI Person": dni_person})
    if person_data:
        education_data = person_data.get("Education History")
        if education_data:
            return education_data
        else:
            raise Exception(f"No educational history found for DNI {dni_person}")
    else:
        raise Exception(f"No person found for DNI {dni_person}")


def get_fine_history(dni_person: int):
    person_data = COL_PERSON.find_one({"DNI Person": dni_person})
    if person_data:
        fine_data = person_data.get("Fine History")
        if fine_data:
            return fine_data
        else:
            raise Exception(f"No fine history found for DNI {dni_person}")
    else:
        raise Exception(f"No person found for DNI {dni_person}")


def get_vehicle_history(dni_person: int):
    person_data = COL_PERSON.find_one({"DNI Person": dni_person})
    if person_data:
        vehicle_data = person_data.get("Vehicle History")
        if vehicle_data:
            return vehicle_data
        else:
            raise Exception(f"No vehicle history found for DNI {dni_person}")
    else:
        raise Exception(f"No person found for DNI {dni_person}")


def get_case_history(dni_person: int):
    person_data = COL_PERSON.find_one({"DNI Person": dni_person})
    if person_data:
        medical_data = person_data.get("Case History")
        if medical_data:
            return medical_data
        else:
            raise Exception(f"No medical history found for DNI {dni_person}")
    else:
        raise Exception(f"No person found for DNI {dni_person}")


def get_medical_history(dni_person: int):
    person_data = COL_PERSON.find_one({"DNI Person": dni_person})
    if person_data:
        medical_data = person_data.get("Medical History")
        if medical_data:
            return medical_data
        else:
            raise Exception(f"No medical history found for DNI {dni_person}")
    else:
        raise Exception(f"No person found for DNI {dni_person}")


class Mediator:
    def __init__(self):
        self._education_histories = []
        self._fine_histories = []
        self._case_histories = []
        self._medical_histories = []
        self._vehicle_histories = []
        self._persons = []
        self.load_data()

    def load_data(self):
        for person in COL_PERSON.find():
            if "_id" in person:
                del person["_id"]
            self._persons.append(person)
        for educational_history in COL_EDUCATION_HISTORY.find():
            self._education_histories.append(educational_history)
        for fine_history in COL_FINE_HISTORY.find():
            self._fine_histories.append(fine_history)
        for vehicle_history in COL_VEHICLE_HISTORY.find():
            self._vehicle_histories.append(vehicle_history)
        for case_history in COL_CASE_HISTORY.find():
            self._case_histories.append(case_history)
        for medical_history in COL_MEDICAL_HISTORY.find():
            self._medical_histories.append(medical_history)

    # Create Person
    def add_person(self, person: Person = Person()):
        person_dict = person.to_dict()
        if not any(p["DNI Person"] == person.dni for p in self._persons):
            self._persons.append(person_dict)
            person.mediator = self
            print(f"Added person: {person.name}")
            COL_PERSON.insert_one(person.to_dict())
        else:
            print(f"Person with DNI {person.dni} already exists.")

    # Link histories with people

    def link_education_history_to_person(self, dni_person: int,
                                         education_history: EducationHistory = EducationHistory()):
        history_dic = education_history.to_dict()
        for p in self._persons:
            if p["DNI Person"] == dni_person:
                p["Education History"] = history_dic
                COL_PERSON.update_one({"DNI Person": dni_person},
                                      {"$set": {"Education History": history_dic}})
                print(f"Linked educational history for DNI {education_history.dni_person}")
                return history_dic
        raise Exception(f"No person found for DNI {dni_person}")

    def link_fine_history_to_person(self, dni_person: int, fine_history: FineHistory = FineHistory()):
        history_dic = fine_history.to_dict()
        for p in self._persons:
            if p["DNI Person"] == dni_person:
                p["Fine History"] = history_dic
                COL_PERSON.update_one({"DNI Person": dni_person},
                                      {"$set": {"Fine History": history_dic}})
                print(f"Linked fine history for DNI {fine_history.dni_person}")
                return history_dic
        raise Exception(f"No person found for DNI {dni_person}")

    def link_vehicle_history_to_person(self, dni_person: int, vehicle_history: VehicleHistory = VehicleHistory()):
        history_dic = vehicle_history.to_dict()
        for p in self._persons:
            if p["DNI Person"] == dni_person:
                p["Vehicle History"] = history_dic
                COL_PERSON.update_one({"DNI Person": dni_person},
                                      {"$set": {"Vehicle History": history_dic}})
                print(f"Linked vehicle history for DNI {vehicle_history.dni_person}")
                return history_dic
        raise Exception(f"No person found for DNI {dni_person}")

    def link_case_history_to_person(self, dni_person: int, case_history: CaseHistory = CaseHistory()):
        history_dic = case_history.to_dict()
        for p in self._persons:
            if p["DNI Person"] == dni_person:
                p["Case History"] = history_dic
                COL_PERSON.update_one({"DNI Person": dni_person},
                                      {"$set": {"Case History": history_dic}})
                print(f"Linked case history for DNI {case_history.dni_person}")
                return history_dic
        raise Exception(f"No person found for DNI {dni_person}")

    def link_medical_history_to_person(self, dni_person: int, medical_history: MedicalHistory = MedicalHistory()):
        history_dic = medical_history.to_dict()
        for p in self._persons:
            if p["DNI Person"] == dni_person:
                p["Medical History"] = history_dic
                COL_PERSON.update_one({"DNI Person": dni_person},
                                      {"$set": {"Medical History": history_dic}})
                print(f"Linked medical history for DNI {medical_history.dni_person}")
                return history_dic
        raise Exception(f"No person found for DNI {dni_person}")

    def get_persons(self):
        if len(self._persons) == 0:
            raise Exception('No data yet')
        return self._persons
