from datetime import date
from flyweight.flyweight_address import AddressFlyweightFactory, add_address_to_database
from flyweight.flyweight_agency import AgencyFlyweightFactory, add_agency_to_database
from logic.address import address1, address2
from logic.agency import agency1

if __name__ == "__main__":
    factory = AddressFlyweightFactory([
        ["123 Main St", 5, "Apt 3B", "1010", "City Ville", "State Ville", "Country Land"],
        ["456 Elm St", 10, "None", "2020", "Towns Ville", "State Ville", "Country Land"],
        ["789 Oak St", 15, "Apt 2C", "3030", "Villa Getan", "State Ville", "Country Land"],
    ])

    factory.list_flyweights()

    add_address_to_database(
        factory, address1.street, address1.number, address1.apartment, address1.postal_code, address1.locality,
        address1.department, address1.country)

    add_address_to_database(
        factory, "456 Elm St", 10, None, "2020", "Towns Ville", "State Ville", "Country Land")

    print("\n")

    factory.list_flyweights()
    factory = AgencyFlyweightFactory([
            ["965816", "52173", "Tis er ium", "3145975012", address2.__str__(), "5", "10", "2023", str(date.today())],
            ["819911", "82910", "Bom Spit", "3004689813", address2.__str__(), "9", "11", "2022", str(date.today())],
            ["961812", "42173", "Dis er", "31459112312", address2.__str__(), "10", "1", "2021", str(date.today())],
        ])

    factory.list_flyweights()
    add_agency_to_database(
            factory, agency1.id_entity, agency1.nit, agency1.business_name, agency1.contact, agency1.address,
            agency1.day, agency1.month, agency1.year)

    add_agency_to_database(factory, 965816, 52173, "Tis er ium", "3145975012", address=address2, day=5, month=10,
                           year=2023, date_actualization=date.today())
    print("\n")
    factory.list_flyweights()
