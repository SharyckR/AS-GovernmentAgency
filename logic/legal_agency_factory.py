from datetime import datetime
from pydantic import BaseModel
from legal_entity import LegalEntity
from address import Address


class Agency(LegalEntity, BaseModel):
    id_agency: int
    entity: str = 'entity'
    name: str
    nit: int
    contact: str
    address: Address
    permission: int
    date_actualization: datetime = datetime.now()

    def __str__(self):
        return '({0},{1},{2},{3},{4},{5},{6},{7})'.format(self.id_agency, self.entity, self.name,
                                                          self.nit, self.contact, self.address.__str__(),
                                                          self.permission, self.date_actualization)

    def __eq__(self, other):
        if isinstance(other, Agency):
            return(self.id_agency == other.id_agency and self.entity == other.entity and self.name == other.name and
                   self.nit == other.nit and self.contact == other.contact and
                   self.address.__eq__(other.address) and self.permission == other.permission and
                   self.date_actualization == other.date_actualization)
