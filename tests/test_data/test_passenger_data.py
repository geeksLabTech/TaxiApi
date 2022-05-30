from ...models import PassengerDB

PASSENGER_ONE = {
    "id": 1,
    "name": "John Doe",
    "phone_number": "55193109",
    "password": "12345"
}

PASSENGER_TWO = {
    "id": 2,
    "name": "Jane Doe",
    "phone_number": "55193111",
    "password": "54321"
}

PASSENGER_THREE = {
    "id": 3,
    "name": "John Smith",
    "phone_number": "55193112",
    "password": "abc123"
}

PASSENGER_FOUR = {
    "id": 4,
    "name": "Jane Smith",
    "phone_number": "55193113",
    "password": "abc123"
}


PASSENGER_DB_ONE = PassengerDB(id=1, name="John Doe", phone_number="55193109", password="12345")
#PASSENGER_DB_TWO = PassengerDB(**PASSENGER_TWO)
#PASSENGER_DB_THREE = PassengerDB(**PASSENGER_THREE)
#PASSENGER_DB_FOUR = PassengerDB(**PASSENGER_FOUR)


PASSENGERS_DB = [PASSENGER_DB_ONE]#, PASSENGER_DB_TWO, PASSENGER_DB_THREE, PASSENGER_DB_FOUR]