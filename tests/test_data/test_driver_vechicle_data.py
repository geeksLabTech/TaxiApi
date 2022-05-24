# Fake data of DriverVehicle scheme for testing database
from ...models import DriverVehicleDB

DRIVER_VEHICLE_ONE = {
    "driver_id": 1,
    "vehicle_id": 1
}

DRIVER_VEHICLE_TWO = {
    "driver_id": 2,
    "vehicle_id": 2
}

DRIVER_VEHICLE_THREE = {
    "driver_id": 3,
    "vehicle_id": 3
}

DRIVER_VEHICLE_DB_ONE = DriverVehicleDB(**DRIVER_VEHICLE_ONE)
DRIVER_VEHICLE_DB_TWO = DriverVehicleDB(**DRIVER_VEHICLE_TWO)
DRIVER_VEHICLE_DB_THREE = DriverVehicleDB(**DRIVER_VEHICLE_THREE)

DRIVERS_VEHICLES_DB = [DRIVER_VEHICLE_DB_ONE, DRIVER_VEHICLE_DB_TWO, DRIVER_VEHICLE_DB_THREE]