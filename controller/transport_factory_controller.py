from typing import List
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.transport_factory import TransportFactory
from logic.fine_history import FineHistory
from logic.vehicle_history import VehicleHistory

MY_CLIENT = MongoClient('mongodb://as-database:oHfA0NSURbklPgc5DVeLDnxDy1KaSHNJVrji28EMMT4FSrk'
                        '4bandpHgx7qRYlgWRTx8g8wnr2rZ9ACDbpCZ30g==@as-database.mongo.cosmos.azure.com:10255'
                        '/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@as-'
                        'database@')
MY_DB = MY_CLIENT['Entity']
TRANSPORT_AGENCY = MY_DB['Transport Agency']
HISTORIES = MY_CLIENT['Histories']
COL_FINE_HISTORY = HISTORIES['Fine History']
COL_VEHICLE_HISTORY = HISTORIES['Vehicle History']


class TransportFactoryController:
    def __init__(self):
        self._transport_factory: TransportFactory = TransportFactory()
        self._transport_agencies: List = []
        self._fine_histories: List = []
        self._vehicle_histories: List = []
        self.load_data()

    def load_data(self):
        for transport_agency in TRANSPORT_AGENCY.find():
            if '_id' in transport_agency:
                del transport_agency['_id']
            self._transport_agencies.append(transport_agency)
        for fine_history in COL_FINE_HISTORY.find():
            if '_id' in fine_history:
                del fine_history['_id']
            self._fine_histories.append(fine_history)
        for vehicle_history in COL_VEHICLE_HISTORY.find():
            if '_id' in vehicle_history:
                del vehicle_history['_id']
            self._vehicle_histories.append(vehicle_history)

    def add_transport_agency(self, agency: AgencyFactory = AgencyFactory()):
        transport_agency = self._transport_factory.create_agency(agency=agency)
        transport_agency_dict = transport_agency.to_dict()
        if not any(ea['Agency']['ID Entity'] == agency.id_entity for ea in self._transport_agencies):
            self._transport_agencies.append(transport_agency_dict)
            print(f'{transport_agency.__class__.__name__} Added\n')
            TRANSPORT_AGENCY.insert_one(transport_agency_dict)
            if '_id' in transport_agency_dict:
                del transport_agency_dict['_id']
            return transport_agency_dict
        else:
            raise Exception(f'Agency with ID ENTITY: {agency.id_entity} already exists')

    def update_transport_agency(self, id_entity, agency):
        for ea in self._transport_agencies:
            if ea['Agency']['ID Entity'] == id_entity:
                update_operation = UpdateOne({"Agency.ID Entity": agency.id_entity},
                                             {"$set": {"Agency": agency.to_dict()}})
                TRANSPORT_AGENCY.bulk_write([update_operation])
                ea['Agency'] = agency.to_dict()
                print(f'Agency with ID Entity: {agency.id_entity} updated')
                return agency.to_dict()
        raise Exception(f'Does not exist an agency with ID Entity : {id_entity}')

    def add_fine_history(self, fine_history: FineHistory = FineHistory()):
        fine_history_dict = fine_history.to_dict()
        if not any(eh['DNI Person'] == fine_history.dni_person for eh in self._fine_histories):
            self._fine_histories.append(fine_history_dict)
            print(f'{fine_history.__class__.__name__} added\n')
            COL_FINE_HISTORY.insert_one(fine_history_dict)
            return fine_history_dict
        else:
            raise Exception(f'Fine History with ID HISTORY: {fine_history.dni_person} already exist')

    def add_vehicle_history(self, vehicle_history: VehicleHistory = VehicleHistory()):
        vehicle_history_dict = vehicle_history.to_dict()
        if not any(eh['DNI Person'] == vehicle_history.dni_person for eh in self._vehicle_histories):
            self._vehicle_histories.append(vehicle_history_dict)
            print(f'{vehicle_history.__class__.__name__} added\n')
            COL_VEHICLE_HISTORY.insert_one(vehicle_history_dict)
            return vehicle_history_dict
        else:
            raise Exception(f'Vehicle History with ID HISTORY: {vehicle_history.dni_person} already exist')

    def link_transport_agency_with_fine_history(self, id_transport_agency: int,
                                                fine_history: FineHistory = FineHistory()):
        fine_history_dict = fine_history.to_dict()
        for le in self._transport_agencies:
            if le['Agency']['ID Entity'] == id_transport_agency:
                update_operation = UpdateOne({"Agency.ID Entity": id_transport_agency},
                                             {"$set": {"Fine History": fine_history_dict}})
                le['Fine History'] = fine_history_dict
                TRANSPORT_AGENCY.bulk_write([update_operation])
                print(f'Linked {fine_history.__class__.__name__} with {id_transport_agency} of Transport Agency')
                return fine_history_dict
        raise Exception(f'ID Entity: {id_transport_agency} not found.')

    def link_transport_agency_with_vehicle_history(self, id_transport_agency: int,
                                                   vehicle_history: VehicleHistory = VehicleHistory()):
        vehicle_history_dict = vehicle_history.to_dict()
        for le in self._transport_agencies:
            if le['Agency']['ID Entity'] == id_transport_agency:
                update_operation = UpdateOne({"Agency.ID Entity": id_transport_agency},
                                             {"$set": {"Vehicle History": vehicle_history_dict}})
                le['Vehicle History'] = vehicle_history_dict
                TRANSPORT_AGENCY.bulk_write([update_operation])
                print(f'Linked {vehicle_history.__class__.__name__} with {id_transport_agency} of Transport Agency')
                return vehicle_history_dict
        raise Exception(f'ID Entity: {id_transport_agency} not found.')

    def get_transport_agencies(self):
        if len(self._transport_agencies) == 0:
            raise Exception('No data yet')
        return self._transport_agencies

    def get_fine_histories(self):
        if len(self._fine_histories) == 0:
            raise Exception('No data yet')
        return self._fine_histories

    def get_vehicle_histories(self):
        if len(self._vehicle_histories) == 0:
            raise Exception('No data yet')
        return self._vehicle_histories
