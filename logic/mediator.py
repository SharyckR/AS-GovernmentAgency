
class Mediator:
    def __init__(self):
        self.persons = []
        self.education_histories = []
        self.fine_histories = []
        self.case_histories = []
        self.medical_histories = []
        self.vehicle_histories = []

    # Create classes

    def add_person(self, person):
        self.persons.append(person)
        person.mediator = self
        print(f"Added person: {person.name}")

    def add_education_history(self, education_history):
        self.education_histories.append(education_history)
        education_history.mediator = self
        print(f"Educational history added for DNI {education_history.dni_person}")

    def add_fine_history(self, fine_history):
        self.fine_histories.append(fine_history)
        fine_history.mediator = self
        print(f"Fine history added for DNI {fine_history.dni_person}")

    def add_vehicle_history(self, vehicle_history):
        self.vehicle_histories.append(vehicle_history)
        vehicle_history.mediator = self
        print(f"Vehicle history added for DNI {vehicle_history.dni_person}")

    def add_case_history(self, case_history):
        self.case_histories.append(case_history)
        case_history.mediator = self
        print(f"Case history added for DNI {case_history.dni_person}")

    def add_medical_history(self, medical_history):
        self.medical_histories.append(medical_history)
        medical_history.mediator = self
        print(f"Medical history added for DNI {medical_history.dni_person}")

    # Link histories with people

    def link_education_history_to_person(self, education_history, person):
        if education_history in self.education_histories and person in self.persons:
            person.education_history = education_history
            print(f"Linked educational history for DNI {education_history.dni_person}")

    def link_fine_history_to_person(self, fine_history, person):
        if fine_history in self.fine_histories and person in self.persons:
            person.fine_history = fine_history
            print(f"Linked fine history for DNI {fine_history.dni_person}")

    def link_vehicle_history_to_person(self, vehicle_history, person):
        if vehicle_history in self.vehicle_histories and person in self.persons:
            person.vehicle_history = vehicle_history
            print(f"Linked vehicle history for DNI {vehicle_history.dni_person}")

    def link_case_history_to_person(self, case_history, person):
        if case_history in self.case_histories and person in self.persons:
            person.case_history = case_history
            print(f"Linked case history for DNI {case_history.dni_person}")

    def link_medical_history_to_person(self, medical_history, person):
        if medical_history in self.medical_histories and person in self.persons:
            person.medical_history = medical_history
            print(f"Linked medical history for DNI {medical_history.dni_person}")

    # History search by ID

    def get_person_by_dni(self, dni):
        for person in self.persons:
            if person.dni == dni:
                return person

    def get_education_history_by_dni(self, dni):
        for education_history in self.education_histories:
            if education_history.dni_person == dni:
                return education_history

    def get_fine_history_by_dni(self, dni):
        for fine_history in self.fine_histories:
            if fine_history.dni_person == dni:
                return fine_history

    def get_vehicle_history_by_dni(self, dni):
        for vehicle_history in self.vehicle_histories:
            if vehicle_history.dni_person == dni:
                return vehicle_history

    def get_case_history_by_dni(self, dni):
        for case_history in self.case_histories:
            if case_history.dni_person == dni:
                return case_history

    def get_medical_history_by_dni(self, dni):
        for medical_history in self.medical_histories:
            if medical_history.dni_person == dni:
                return medical_history
