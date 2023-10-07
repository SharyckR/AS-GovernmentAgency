from abc import ABC, abstractmethod
from pydantic import BaseModel
from agency_factory import Agency
from entity import Entity


class NaturalEntity(Entity):
    def kind_of_entity(self):
        return 'Natural entity'


class LegalEntity(Entity):
    def kind_of_entity(self):
        return 'Legal entity'

