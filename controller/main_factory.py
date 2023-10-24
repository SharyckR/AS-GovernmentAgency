from controller.legal_factory_controller import LegalFactoryController
from controller.transport_factory_controller import TransportFactoryController
from logic.agency_factory import *
from logic.case_history import *
from logic.vehicle_history import *
from logic.fine_history import *
from logic.education_history import edu_history2
from controller.health_factory_controller import HealthFactoryController
from controller.educational_factory_controller import EducationalFactoryController
from logic.agency_factory import agency1, agency2
from logic.educational_factory import *
from logic.medical_history import medical_history1

if __name__ == '__main__':
    educational_factory_controller = EducationalFactoryController()
    health_factory_controller = HealthFactoryController()
    try:
        educational_factory_controller.add_educational_agency(agency2, ['First places 2'])
        health_factory_controller.add_health_agency(agency1)
    except Exception as e:
        print(e)
    data = educational_factory_controller.link_agency_with_history(agency2.id_entity, edu_history2)
    data_2 = health_factory_controller.link_agency_with_history(agency1.id_entity, medical_history1)
    ed_history = {
        "id_history": 424234,
        "dni_person": 14123213,
        "education": "Height level",
        "name_institution": "Institution Name",
        "location": {
            "street": "123 Main St",
            "number": 5,
            "apartment": "Apt 3B",
            "postal_code": "1010",
            "locality": "City Ville",
            "department": "State Ville",
            "country": "Country Land"
        },
        "title_obtained": "Title Obtained",
        "day": 14,
        "month": 1,
        "year": 2023
    }
    medical_history = {
        "id_history": 13, "dni_person": 1043638720, "type_blood": "O+", "pathologies": "None",
        "description_treatment": "Wound healing",
        "doctor_charge": "Kevin Rodriguez", "day": 5, "month": 10, "year": 2023
    }
    edu_history = educational_factory_controller.add_ed_history(ed_history)
    print(edu_history.__str__())
    med_history = health_factory_controller.add_md_history(medical_history)
    print(med_history.__str__())

    # Initial test of Legal Factory Controller

    legal_factory_controller = LegalFactoryController()
    agency_update = AgencyFactory(id_entity=10290294, entity=LegalEntity(), nit=4224, business_name="Business Name",
                                  contact="31459750", address=address2, day=5, month=10, year=2023)
    try:
        legal_factory_controller.add_legal_agency(agency2)
        legal_factory_controller.update_legal_agency(agency2.id_entity, agency_update)
        legal_factory_controller.add_case_history(case_history2)
    except Exception as e:
        print(e)
    legal_factory_controller.link_legal_agency_with_history(agency2.id_entity, case_history2)

    # Initial test of Transport Factory Controller

    transport_factory_controller = TransportFactoryController()
    agency_update = AgencyFactory(id_entity=10290294, entity=LegalEntity(), nit=4224, business_name="Business Name",
                                  contact="31459750", address=address2, day=5, month=10, year=2023)
    try:
        transport_factory_controller.add_transport_agency(agency2)
        transport_factory_controller.update_transport_agency(agency2.id_entity, agency_update)
        transport_factory_controller.add_fine_history(fine_history1)
        transport_factory_controller.add_vehicle_history(vehicle_history1)
    except Exception as e:
        print(e)
    transport_factory_controller.link_transport_agency_with_fine_history(agency2.id_entity, fine_history1)
    transport_factory_controller.link_transport_agency_with_vehicle_history(agency2.id_entity, vehicle_history1)
