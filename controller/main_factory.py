from educational_factory_controller import EducationalFactoryController
from logic.agency_factory import *
from logic.education_history import *

if __name__ == '__main__':
    educational_factory_controller = EducationalFactoryController()
    try:
        educational_factory_controller.add_agency(agency2, ['First places 2'])
    except Exception as e:
        print(e)
    data = educational_factory_controller.link_agency_with_history(agency2.id_entity, edu_history2)
