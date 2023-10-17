<<<<<<< HEAD
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
=======
import json
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0


class Mediator:
    def __init__(self):
<<<<<<< HEAD
=======
        self.load_data()
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0
        self.education_histories = []
        self.fine_histories = []
        self.case_histories = []
        self.medical_histories = []
        self.vehicle_histories = []
        self.persons = []
        self.load_data()

    def load_data(self):
<<<<<<< HEAD
        self.persons = []
        for person in COL_PERSON.find():
            if "_id" in person:
                del person["_id"]
            self.persons.append(person)
        for educational_history in COL_EDUCATION_HISTORY.find():
            if "_id" in educational_history:
                del COL_EDUCATION_HISTORY["_id"]
            self.education_histories.append(educational_history)
        for fine_history in COL_FINE_HISTORY.find():
            self.fine_histories.append(fine_history)
        for vehicle_history in COL_VEHICLE_HISTORY.find():
            self.vehicle_histories.append(vehicle_history)
        for case_history in COL_CASE_HISTORY.find():
            self.case_histories.append(case_history)
        for medical_history in COL_MEDICAL_HISTORY.find():
            self.medical_histories.append(medical_history)

    def add_person(self, person: Person = Person()):
        person_dict = person.to_dict()
        print(self.persons)
=======
        try:
            with open("storage.json", "r") as json_file:
                data = json.load(json_file)
                self.education_histories = data.get("education_histories", [])
                self.fine_histories = data.get("fine_histories", [])
                self.case_histories = data.get("case_histories", [])
                self.medical_histories = data.get("medical_histories", [])
                self.vehicle_histories = data.get("vehicle_histories", [])
                self.persons = data.get("persons", [])

        except FileNotFoundError:
            self.education_histories = []
            self.fine_histories = []
            self.case_histories = []
            self.medical_histories = []
            self.vehicle_histories = []
            self.persons = []

    def save_data(self):
        data = {
            "education_histories": self.education_histories,
            "fine_histories": self.fine_histories,
            "case_histories": self.case_histories,
            "medical_histories": self.medical_histories,
            "vehicle_histories": self.vehicle_histories,
            "persons": self.persons
        }
        with open("storage.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    # Create classes

    def add_person(self, person):
        person_dict = person.to_dict()
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0
        if not any(p["DNI Person"] == person.dni for p in self.persons):
            self.persons.append(person_dict)
            person.mediator = self
            print(f"Added person: {person.name}")
<<<<<<< HEAD
            COL_PERSON.insert_one(person.to_dict())
        else:
            print(f"Person with DNI {person.dni} already exists.")

    def link_education_history_to_person(self, dni_person: int,
                                         education_history: EducationHistory = EducationHistory()):
        history_dic = education_history.to_dict()
        for p in self.persons:
            if p["DNI Person"] == dni_person:
                p["Education History"] = history_dic
                COL_PERSON.update_one({"DNI Person": dni_person},
                                      {"$set": {"Education History": history_dic}})
                print(f"Linked educational history for DNI {education_history.dni_person}")
                return history_dic
        raise Exception(f"No person found for DNI {dni_person}")

    def link_fine_history_to_person(self, dni_person: int, fine_history: FineHistory = FineHistory()):
        history_dic = fine_history.to_dict()
        for p in self.persons:
            if p["DNI Person"] == dni_person:
                p["Fine History"] = history_dic
                update = COL_PERSON.update_one({"DNI Person": dni_person},
                                               {"$set": {"Fine History": history_dic}})
                print(f"Linked fine history for DNI {fine_history.dni_person}")
                return update
        raise Exception(f"No person found for DNI {dni_person}")

    def link_vehicle_history_to_person(self, dni_person: int, vehicle_history: VehicleHistory = VehicleHistory()):
        history_dic = vehicle_history.to_dict()
        for p in self.persons:
            if p["DNI Person"] == dni_person:
                p["Vehicle History"] = history_dic
                update = COL_PERSON.update_one({"DNI Person": dni_person},
                                               {"$set": {"Vehicle History": history_dic}})
                print(f"Linked vehicle history for DNI {vehicle_history.dni_person}")
                return update
        raise Exception(f"No person found for DNI {dni_person}")

    def link_case_history_to_person(self, dni_person: int, case_history: CaseHistory = CaseHistory()):
        history_dic = case_history.to_dict()
        for p in self.persons:
            if p["DNI Person"] == dni_person:
                p["Case History"] = history_dic
                update = COL_PERSON.update_one({"DNI Person": dni_person},
                                               {"$set": {"Case History": history_dic}})
                print(f"Linked case history for DNI {case_history.dni_person}")
                return update
        raise Exception(f"No person found for DNI {dni_person}")

    def link_medical_history_to_person(self, dni_person: int, medical_history: MedicalHistory = MedicalHistory()):
        history_dic = medical_history.to_dict()
        for p in self.persons:
            if p["DNI Person"] == dni_person:
                p["Medical History"] = history_dic
                update = COL_PERSON.update_one({"DNI Person": dni_person},
                                               {"$set": {"Medical History": history_dic}})
                print(f"Linked medical history for DNI {medical_history.dni_person}")
                return update
        raise Exception(f"No person found for DNI {dni_person}")

    def get_persons(self):
        if len(self.persons) == 0:
            raise Exception('No data yet')
        return self.persons
=======
            self.save_data()
        else:
            print(f"Person with DNI {person.dni} already exists.")

    def add_history(self, history_list, history_item, dni_person):
        history_dict = history_item.to_dict()
        for history in history_list:
            if history["DNI Person"] == dni_person:
                history.update(history_dict)
                history_item.mediator = self
                print(f"{history_item.__class__.__name__} updated for DNI {dni_person}")
                self.save_data()
                return

        history_list.append(history_dict)
        history_item.mediator = self
        print(f"{history_item.__class__.__name__} added for DNI {dni_person}")
        self.save_data()

    def add_education_history(self, education_history):
        self.add_history(self.education_histories, education_history, education_history.dni_person)

    def add_fine_history(self, fine_history):
        self.add_history(self.fine_histories, fine_history, fine_history.dni_person)

    def add_vehicle_history(self, vehicle_history):
        self.add_history(self.vehicle_histories, vehicle_history, vehicle_history.dni_person)

    def add_case_history(self, case_history):
        self.add_history(self.case_histories, case_history, case_history.dni_person)

    def add_medical_history(self, medical_history):
        self.add_history(self.medical_histories, medical_history, medical_history.dni_person)

    # Link histories with people

    def link_education_history_to_person(self, education_history, person):
        # Busca la persona con el mismo DNI en la lista de personas
        for p in self.persons:
            if p["DNI Person"] == person.dni:
                p["Education History"] = education_history.to_dict()
                self.save_data()
                print(f"Linked educational history for DNI {education_history.dni_person}")
                return
        print(f"No person found for DNI {person.dni}")

    def link_fine_history_to_person(self, fine_history, person):
        for p in self.persons:
            if p["DNI Person"] == person.dni:
                p["Fine History"] = fine_history.to_dict()
                self.save_data()
                print(f"Linked fine history for DNI {fine_history.dni_person}")
                return
        print(f"No person found for DNI {person.dni}")

    def link_vehicle_history_to_person(self, vehicle_history, person):
        for p in self.persons:
            if p["DNI Person"] == person.dni:
                p["Vehicle History"] = vehicle_history.to_dict()
                self.save_data()
                print(f"Linked vehicle history for DNI {vehicle_history.dni_person}")
                return
        print(f"No person found for DNI {person.dni}")

    def link_case_history_to_person(self, case_history, person):
        for p in self.persons:
            if p["DNI Person"] == person.dni:
                p["Case History"] = case_history.to_dict()
                self.save_data()
                print(f"Linked case history for DNI {case_history.dni_person}")
                return
        print(f"No person found for DNI {person.dni}")

    def link_medical_history_to_person(self, medical_history, person):
        for p in self.persons:
            if p["DNI Person"] == person.dni:
                p["Medical History"] = medical_history.to_dict()
                self.save_data()
                print(f"Linked medical history for DNI {medical_history.dni_person}")
                return
        print(f"No person found for DNI {person.dni}")

    # History search by ID

    def get_person_by_dni(self, dni):
        for person in self.persons:
            if person.get("DNI Person") == dni:
                if person:
                    return person
                else:
                    return f"Person with DNI {dni} not found."
        return None

    def find_history_by_dni(self, history_list, dni):
        for history in history_list:
            if history.get("DNI Person") == dni:
                if history:
                    return history
                else:
                    return f"History for DNI {dni} not found."
        return None

    def get_education_history_by_dni(self, dni):
        return self.find_history_by_dni(self.education_histories, dni)

    def get_fine_history_by_dni(self, dni):
        return self.find_history_by_dni(self.fine_histories, dni)

    def get_vehicle_history_by_dni(self, dni):
        return self.find_history_by_dni(self.vehicle_histories, dni)

    def get_case_history_by_dni(self, dni):
        return self.find_history_by_dni(self.case_histories, dni)

    def get_medical_history_by_dni(self, dni):
        return self.find_history_by_dni(self.medical_histories, dni)
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0
