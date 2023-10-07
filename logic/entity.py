from pydantic import BaseModel


class EntityFactory(BaseModel):
    id_entity: int
    type: str

    def __str__(self):
        return '({0},{1})'.format(self.id_entity, self.type)

    def __eq__(self, other):
        if isinstance(other,EntityFactory):
            return self.id_entity == other.id_entity and self.type == other.type
        return False
