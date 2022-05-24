
from ...models import DriverDB


DRIVER_ONE = {
    "id": 1,
    "name": "Leonardo",
    "phone_number": "51321321",
    "password": "12345"
}

DRIVER_TWO = {
    "id": 2,
    "name": "Donatello",
    "phone_number": "51321322",
    "password": "54321"
}

DRIVER_THREE = {
    "id": 3,
    "name": "Raphael",
    "phone_number": "51321323",
    "password": "abc123"
}

DRIVER_FOUR = {
    "id": 4,
    "name": "Michaelangelo",
    "phone_number": "51321324",
    "password": "abc123"
}


DRIVER_DB_ONE = DriverDB(id=1, name="Leonardo", phone_number="51321321", password="12345")
DRIVER_DB_TWO = DriverDB(**DRIVER_TWO)
DRIVER_DB_THREE = DriverDB(**DRIVER_THREE)
DRIVER_DB_FOUR = DriverDB(**DRIVER_FOUR)

DRIVERS_DB = [DRIVER_ONE, DRIVER_TWO, DRIVER_THREE, DRIVER_FOUR]