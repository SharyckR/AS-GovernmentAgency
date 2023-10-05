from pydantic import BaseModel


class VehicleHistory(BaseModel):
    information_person: object
    vehicle: str
    type_vehicle: str
    description_vehicle: str
    plate_vehicle: str

    def __str__(self) -> str:
        return '({0},{1},{2},{3},{4})'.format(self.information_person, self.vehicle, self.type_vehicle,
                                              self.description_vehicle, self.plate_vehicle)

    def __eq__(self, other) -> bool:
        if isinstance(other, VehicleHistory):
            return (self.information_person == other.information_person and self.vehicle == other.vehicle and
                    self.type_vehicle == other.type_vehicle and
                    self.description_vehicle == other.description_vehicle and
                    self.plate_vehicle == other.plate_vehicle)
