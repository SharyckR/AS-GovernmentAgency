from entity import Entity


class NaturalEntity(Entity):
    type = 'Natural entity'

    def kind_of_entity(self):
        return self.type
