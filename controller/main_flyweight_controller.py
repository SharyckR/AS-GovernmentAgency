from controller.flyweight_address_controller import FlyAddressController

flyweight_controller = FlyAddressController()

try:
    for value in list(flyweight_controller.get_address().values()):
        print('Values: ', value.shared_state)
    print("\n\n\n")

except Exception as e:
    print(e)
finally:
    address = {"street": '123 Main St', "number": 5, "apartment": 'Apt 3B', "postal_code": '1010',
               "locality": 'City Ville', "department": 'State Ville', "country": 'Country Land'}

    flyweight_controller.add_address_to_database(address)

