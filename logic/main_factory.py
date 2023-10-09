from datetime import date
from logic.educational_factory import EducationalFactory
from logic.health_factory import HealthFactory
from logic.legal_factory import LegalFactory
from logic.transport_factory import TransportFactory
from logic.address import address1
from logic.agency_factory import agency1, agency2
from logic.case_history import case_history1
from logic.education_history import edu_history1
from logic.fine_history import fine_history1
from logic.medical_history import medical_history1
from logic.vehicle_history import vehicle_history1


if __name__ == '__main__':
    educational_factory = EducationalFactory()
    health_factory = HealthFactory()
    legal_factory = LegalFactory()
    transport_factory = TransportFactory()

    edu_agency = educational_factory.create_agency(agency=agency1, education_history=edu_history1,
                                                   academic_achievements=['Good work', 'High recommended'])

    edu_history = educational_factory.create_history(dni_person=5120167, education="Secondary",
                                                     name_institution="Collage", location=address1,
                                                     title_obtained="Graduated", day=13, month=10, year=2020,
                                                     date_graduation=date(year=2020, month=10, day=13))

    h_agency = health_factory.create_agency(agency=agency2, medical_history=medical_history1)
    medical_history = health_factory.create_history(dni_person=1043638720, type_blood="O+", pathologies="None",
                                                    description_treatment="Wound healing",
                                                    doctor_charge="Kevin Rodriguez", day=5, month=10, year=2023,
                                                    date_treatment=date(2023, 10, 5))

    leg_agency = legal_factory.create_agency(agency=agency1, legal_history=case_history1)
    legal_history = legal_factory.create_history(dni_person=102132323, case="Heist", arrested="Yes",
                                                 description_case="Stole a necklace", jurisdiction="Disciplinary",
                                                 day=15, year=2021, month=5)

    tr_agency = transport_factory.create_agency(agency=agency1, licence='Yes', type_licence='A1',
                                                information_vehicle=vehicle_history1,
                                                information_fine=fine_history1)

    veh_history = transport_factory.create_history(dni_person=1043638720, licence="Yes", type_licence="A2",
                                                   vehicle="Yes", type_vehicle="Car", description_vehicle="Mazda2",
                                                   plate_vehicle="BJU-521")[0]

    fin_history = transport_factory.create_history(dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                                                   description_fine="The person was going more than 100k/h",
                                                   paid="No")[1]

    print(f'Info educational agency: {edu_agency.__str__()}\n\n')
    print(f'Info educational history agency: {edu_history.__str__()}')

    print(f'Info health agency: {h_agency.__str__()}\n\n')
    print(f'Info medical history agency: {medical_history.__str__()}')

    print(f'Info legal agency: {leg_agency.__str__()}\n\n')
    print(f'Info legal history agency: {legal_history.__str__()}')

    print(f'Info transport agency: {tr_agency.__str__()}\n\n')
    print(f'Info fine history agency: {fin_history.__str__()}')
    print(f'Info vehicle history agency: {fin_history.__str__()}')
