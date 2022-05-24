from ...models import FamousPlacesDB

FAMOUS_PLACE_ONE = {
    "id": 1,
    "description": "Place One Description",
    "classification": "Place One Classification",
}

FAMOUS_PLACE_TWO = {
    "id": 2,
    "description": "Place Two Description",
    "classification": "Place Two Classification",
}

FAMOUS_PLACE_THREE = {
    "id": 3,
    "description": "Place Three Description",
    "classification": "Place Three Classification",
}

FAMOUS_PLACE_DB_ONE = FamousPlacesDB(**FAMOUS_PLACE_ONE)
FAMOUS_PLACE_DB_TWO = FamousPlacesDB(**FAMOUS_PLACE_TWO)
FAMOUS_PLACE_DB_THREE = FamousPlacesDB(**FAMOUS_PLACE_THREE)

FAMOUS_PLACES_DB = [FAMOUS_PLACE_DB_ONE, FAMOUS_PLACE_DB_TWO, FAMOUS_PLACE_DB_THREE]