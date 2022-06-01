from ...models import table_trip


TRIP_ONE = {
    "id": 1,
    "driver_id": 1,
    "passenger_id": 1,
    "vehicle_id": 1,
    "date": "2020-01-01",
    "time": "12:00",
    "price": 100.0,
    "status": "ACCEPTED"
}

TRIP_TWO = {
    "id": 2,
    "driver_id": 2,
    "passenger_id": 2,
    "vehicle_id": 2,
    "date": "2020-02-01",
    "time": "23:00",
    "price": 200.0,
    "status": "REJECTED"
}

TRIP_THREE = {
    "id": 3,
    "driver_id": 3,
    "passenger_id": 3,
    "vehicle_id": 3,
    "date": "2020-03-01",
    "time": "8:00",
    "price": 300.0,
    "status": "CANCELED"
}

TRIP_DB_ONE = table_trip(**TRIP_ONE)
TRIP_DB_TWO = table_trip(**TRIP_TWO)
TRIP_DB_THREE = table_trip(**TRIP_THREE)

TRIPS_DB = [TRIP_DB_ONE, TRIP_DB_TWO, TRIP_DB_THREE]