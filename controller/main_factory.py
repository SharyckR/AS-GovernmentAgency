from educational_factory_controller import EducationalFactoryController
from logic.agency_factory import *
from logic.education_history import *

if __name__ == '__main__':
    educational_factory_controller = EducationalFactoryController()

    educational_factory_controller.add_agency(agency2, ['First places'])
    educational_factory_controller.link_agency_with_history(edu_history2, agency2)