from entity import Entity


class LegalEntity(Entity):
    type = 'Legal entity'

    def kind_of_entity(self):
        return self.type

