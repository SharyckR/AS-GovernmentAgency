from agency_factory import Agency, Address, datetime


class HealthAgency(Agency):
    agency_factory: Agency
    medical_history: str

    def __str__(self):
        return '({0}, {1})'.format(
            self.agency_factory.__str__(), self.medical_history
        )

    def __eq__(self, other):
        if isinstance(other, HealthAgency):
            return (self.agency_factory.__eq__(other.agency_factory) and
                    self.medical_history == other.medical_history)
        else:
            return False


if __name__ == '__main__':
    address_instance = Address(
        street="123 Main St",
        city="City",
        state="State",
        zip_code="12345",
        apartment="Apt 101"
    )

    agency_instance = Agency(
        id_agency=1,
        entity='entity',
        name="Agency1",
        nit=1234567890,
        contact="Contacto",
        address=address_instance,
        permission=1,
        date_actualization=datetime.now()
    )

    health1 = HealthAgency(agency_factory=agency_instance, medical_history='medical history 1')
    health2 = HealthAgency(agency_factory=agency_instance, medical_history='medical history 2')

    print(health1.__str__())
    print(health2.__eq__(health1))
