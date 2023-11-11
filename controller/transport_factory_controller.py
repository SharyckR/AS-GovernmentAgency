from os import getenv
from typing import List
from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne
from logic.agency_factory import AgencyFactory
from logic.transport_factory import TransportFactory
from logic.fine_history import FineHistory
from logic.vehicle_history import VehicleHistory

load_dotenv()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
MY_DB = MY_CLIENT["Entity"]
TRANSPORT_AGENCY = MY_DB["Transport Agency"]
HISTORIES = MY_CLIENT["Histories"]
COL_FINE_HISTORY = HISTORIES["Fine History"]
COL_VEHICLE_HISTORY = HISTORIES["Vehicle History"]


class TransportFactoryController:
    def __init__(self):
        self._transport_factory: TransportFactory = TransportFactory()
        self._transport_agencies: List = []
        self._fine_histories: List = []
        self._vehicle_histories: List = []
        self.load_data()

    def load_data(self):
        self._fine_histories = []
        self._vehicle_histories = []
        self._transport_agencies = []
        for transport_agency in TRANSPORT_AGENCY.find():
            if "_id" in transport_agency:
                del transport_agency["_id"]
            self._transport_agencies.append(transport_agency)
        for fine_history in COL_FINE_HISTORY.find():
            if "_id" in fine_history:
                del fine_history["_id"]
            self._fine_histories.append(fine_history)
        for vehicle_history in COL_VEHICLE_HISTORY.find():
            if "_id" in vehicle_history:
                del vehicle_history["_id"]
            self._vehicle_histories.append(vehicle_history)

    def add_transport_agency(self, agency: AgencyFactory):
        self.load_data()
        transport_agency = self._transport_factory.create_agency(agency=agency)
        if not any(le[f"{list(le.keys())[0]}"]["agency"]["id_entity"] == agency.id_entity for le in
                   self._transport_agencies):
            self._transport_agencies.append(transport_agency.to_dict())
            print(f"{transport_agency.__class__.__name__} Added\n")
            TRANSPORT_AGENCY.insert_one(transport_agency.to_dict())
            return transport_agency.to_dict()
        raise Exception(f"Agency with ID ENTITY: {agency.id_entity} already exist")

    def update_transport_agency(self, id_entity, agency):
        self.load_data()
        for ta in self._transport_agencies:
            if ta[f"{list(ta.keys())[0]}"]["agency"]["id_entity"] == id_entity:
                update_operation = UpdateOne({f"{id_entity}.agency.id_entity": agency.id_entity},
                                             {"$set": {f"{id_entity}.agency": agency.to_dict()}})
                TRANSPORT_AGENCY.bulk_write([update_operation])
                ta["Agency"] = agency.to_dict()
                print(f"Agency with ID Entity: {agency.id_entity} updated")
                return agency.to_dict()
        raise Exception(f"Does not exist an agency with ID Entity : {id_entity}")

    def add_fine_history(self, fine_history: dict):
        self.load_data()
        if not any(ca["id_history"] == fine_history["id_history"] for ca in self._fine_histories):
            self._fine_histories.append(fine_history)
            print(f"{fine_history.__class__.__name__} added\n")
            COL_FINE_HISTORY.insert_one(fine_history)
            if "_id" in fine_history:
                del fine_history["_id"]
            return fine_history
        else:
            raise Exception(f"Fine History with ID HISTORY: {fine_history['id_history']} already exist")

    def add_vehicle_history(self, vehicle_history: dict):
        self.load_data()
        if not any(ca["id_history"] == vehicle_history["id_history"] for ca in self._vehicle_histories):
            self._vehicle_histories.append(vehicle_history)
            print(f"{vehicle_history.__class__.__name__} added\n")
            COL_VEHICLE_HISTORY.insert_one(vehicle_history)
            if "_id" in vehicle_history:
                del vehicle_history["_id"]
            return vehicle_history
        else:
            raise Exception(f"Vehicle History with ID HISTORY: {vehicle_history['id_history']} already exist")

    def link_transport_agency_with_fine_history(self, id_transport_agency: int,
                                                fine_history: FineHistory = FineHistory()):
        self.load_data()
        for ta in self._transport_agencies:
            if ta[f"{list(ta.keys())[0]}"]["agency"]["id_entity"] == id_transport_agency:
                update_operation = UpdateOne(
                    {f"{id_transport_agency}.agency.id_entity": id_transport_agency},
                    {"$set": {f"{id_transport_agency}.information_fine": fine_history.to_dict()}})
                ta[f"{id_transport_agency}"]["fine_history"] = fine_history.to_dict()
                TRANSPORT_AGENCY.bulk_write([update_operation])
                print(f"Linked {fine_history.__class__.__name__} with {id_transport_agency} of Transport Agency")
                return fine_history.to_dict()
        raise Exception(f"ID Entity: {id_transport_agency} not found.")

    def link_transport_agency_with_vehicle_history(self, id_transport_agency: int,
                                                   vehicle_history: VehicleHistory = VehicleHistory()):
        self.load_data()
        for ta in self._transport_agencies:
            if ta[f"{list(ta.keys())[0]}"]["agency"]["id_entity"] == id_transport_agency:
                update_operation = UpdateOne(
                    {f"{id_transport_agency}.agency.id_entity": id_transport_agency},
                    {"$set": {f"{id_transport_agency}.information_vehicle": vehicle_history.to_dict()}})
                ta[f"{id_transport_agency}"]["vehicle_history"] = vehicle_history.to_dict()
                TRANSPORT_AGENCY.bulk_write([update_operation])
                print(f"Linked {vehicle_history.__class__.__name__} with {id_transport_agency} of Transport Agency")
                return vehicle_history.to_dict()
        raise Exception(f"ID Entity: {id_transport_agency} not found.")

    def get_transport_agencies(self):
        self.load_data()
        if len(self._transport_agencies) == 0:
            raise Exception("No data yet")
        return self._transport_agencies

    def get_fine_histories(self):
        self.load_data()
        if len(self._fine_histories) == 0:
            raise Exception("No data yet")
        return self._fine_histories

    def get_vehicle_histories(self):
        self.load_data()
        if len(self._vehicle_histories) == 0:
            raise Exception("No data yet")
        return self._vehicle_histories
