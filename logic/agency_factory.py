from pydantic import BaseModel
from address import Address
from datetime import datetime
from legal_entity import LegalEntity


class Agency(LegalEntity, BaseModel):
    id_agency: int = 1
    entity: str = 'entity'
    name: str = 'name'
    nit: int = 1
    contact: str = 'contact'
    address: Address
    permission: int = 1
    date_actualization: datetime = datetime.now()

    @property
    def permission(self) -> int:
        return self.permission

    @permission.setter
    def permission(self, value: int):
        if value not in (0, 1):
            raise ValueError('El campo "permission" debe ser 0 o 1')
        self.permission = value

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(
            self.id_agency, self.entity, self.name,
            self.nit, self.contact, self.address.__str__(),
            self.permission, self.date_actualization
        )

    def __eq__(self, other):
        if isinstance(other, Agency):
            return (self.id_agency == other.id_agency and self.entity == other.entity and
                    self.name == other.name and
                    self.nit == other.nit and self.contact == other.contact and
                    self.address.__eq__(other.address) and self.permission == other.permission and
                    self.date_actualization == other.date_actualization)
        else:
            return False


if __name__ == '__main__':
    address1 = Address(
        street="123 Main St",
        city="City",
        state="State",
        zip_code="12345",
        apartment="Apt 101"
    )

    agency1 = Agency(
        id_agency=1,
        entity='entity',
        name="Agency1",
        nit=1234567890,
        contact="Contacto",
        address=address1,
        permission=1,
        date_actualization=datetime.now()
    )

    address2 = Address(
        street="456 Elm St",
        city="City",
        state="State",
        zip_code="54321",
        apartment="Apt 202"
    )

    agency2 = Agency(
        id_agency=2,
        entity='entity2',
        name="Agency2",
        nit=123456332,
        contact="Contacto",
        address=address2,
        permission=1,
        date_actualization=datetime.now()
    )

    print(agency1.__str__())
    print(agency1.__eq__(agency2))
