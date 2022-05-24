from ...models import PlaceDB


PLACE_ONE = {
    "id": 1,
    "name": "Place One",
    "address": "Place One Address",
    "latitude": 1.0,
    "longitude": 1.0
}

PLACE_TWO = {
    "id": 2,
    "name": "Place Two",
    "address": "Place Two Address",
    "latitude": 2.0,
    "longitude": 2.0
}

PLACE_THREE = {
    "id": 3,
    "name": "Place Three",
    "address": "Place Three Address",
    "latitude": 3.0,
    "longitude": 3.0
}

PLACE_DB_ONE = PlaceDB(**PLACE_ONE)
PLACE_DB_TWO = PlaceDB(**PLACE_TWO)
PLACE_DB_THREE = PlaceDB(**PLACE_THREE)

PLACES_DB = [PLACE_DB_ONE, PLACE_DB_TWO, PLACE_DB_THREE]