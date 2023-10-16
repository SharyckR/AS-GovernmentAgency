import json
import pymongo

my_client = pymongo.MongoClient('mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk'
                                '4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g==@as-database.mongo.cosmos.azure.com:10255'
                                '/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@as-'
                                'database@')

my_db = my_client['Entity']
my_col = my_db['Person']


def find_history_by_dni(history_list, dni):
    for history in history_list:
        if history.get("DNI Person") == dni:
            if history:
                return history
            else:
                return f"History for DNI {dni} not found."
    return None


def convert_object_id_to_str(person):
    person_copy = person.copy()
    if '_id' in person_copy:
        person_copy['_id'] = str(person_copy['_id'])
    return person_copy


class Mediator:
    def __init__(self):
        self.load_data()
        self.education_histories = []
        self.fine_histories = []
        self.case_histories = []
        self.medical_histories = []
        self.vehicle_histories = []
        self.persons = []
        self.load_data()

    def load_data(self):
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
        # Convertir ObjectId a cadenas antes de guardar los datos
        data = {
            "education_histories": self.education_histories,
            "fine_histories": self.fine_histories,
            "case_histories": self.case_histories,
            "medical_histories": self.medical_histories,
            "vehicle_histories": self.vehicle_histories,
            "persons": [convert_object_id_to_str(person) for person in self.persons]
        }
        with open("storage.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

    def add_person(self, person):
        person_dict = person.to_dict()
        if not any(p["DNI Person"] == person.dni for p in self.persons):
            self.persons.append(person_dict)
            person.mediator = self
            print(f"Added person: {person.name}")
            self.save_data()
            return person_dict
        else:
            print(f"Person with DNI {person.dni} already exists.")

    def add_history(self, history_list, history_item, dni_person):
        history_dict = history_item.to_dict()
        if not any(h["DNI Person"] == dni_person for h in history_list):
            history_list.append(history_dict)
            history_item.mediator = self
            print(f"{history_item.__class__.__name__} added for DNI {dni_person}")
            self.save_data()
        else:
            print(f"{history_item.__class__.__name__} for DNI {dni_person} already exists.")

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

    def get_education_history_by_dni(self, dni):
        return find_history_by_dni(self.education_histories, dni)

    def get_fine_history_by_dni(self, dni):
        return find_history_by_dni(self.fine_histories, dni)

    def get_vehicle_history_by_dni(self, dni):
        return find_history_by_dni(self.vehicle_histories, dni)

    def get_case_history_by_dni(self, dni):
        return find_history_by_dni(self.case_histories, dni)

    def get_medical_history_by_dni(self, dni):
        return find_history_by_dni(self.medical_histories, dni)
