
class Mediator:
    def __init__(self):
        self.persons = []
        self.education_histories = []
        self.fine_histories = []

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

    # Link histories with people

    def link_education_history_to_person(self, education_history, person):
        if education_history in self.education_histories and person in self.persons:
            person.education_history = education_history
            print(f"Linked educational history for DNI {education_history.dni_person}")

    def link_fine_history_to_person(self, fine_history, person):
        if fine_history in self.fine_histories and person in self.persons:
            person.fine_history = fine_history
            print(f"Linked fine history for DNI {fine_history.dni_person}")

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
