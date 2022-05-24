from ...models import VehicleDB


VEHICLE_ONE = {
    "id": 1,
    "license_plate": "ABC123",
    "brand": "Toyota",
    "model": "Corolla",
    "color": "White",
    "seats": 5,
    "driver_id": 1,
}

VEHICLE_TWO = {
    "id": 2,
    "license_plate": "DEF456",
    "brand": "Honda",
    "model": "Civic",
    "color": "Black",
    "seats": 5,
    "driver_id": 2,
}

VEHICLE_THREE = {
    "id": 3,
    "license_plate": "GHI789",
    "brand": "Ford",
    "model": "Fiesta",
    "color": "Red",
    "seats": 5,
    "driver_id": 3,
}

VEHICLE_FOUR = {
    "id": 4,
    "license_plate": "JKL012",
    "brand": "Hyundai",
    "model": "Elantra",
    "color": "Blue",
    "seats": 5,
    "driver_id": 4,
}

VEHICLE_DB_ONE = VehicleDB(**VEHICLE_ONE)
VEHICLE_DB_TWO = VehicleDB(**VEHICLE_TWO)
VEHICLE_DB_THREE = VehicleDB(**VEHICLE_THREE)
VEHICLE_DB_FOUR = VehicleDB(**VEHICLE_FOUR)

VECHICLES_DB = [VEHICLE_DB_ONE, VEHICLE_DB_TWO, VEHICLE_DB_THREE, VEHICLE_DB_FOUR]