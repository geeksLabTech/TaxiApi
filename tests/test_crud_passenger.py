from .test_sql_app import client, override_get_db, session
from .test_data.test_passenger_data import PASSENGER_ONE, PASSENGER_TWO, PASSENGER_THREE, PASSENGER_FOUR
from fastapi.testclient import TestClient
from ..main import app
# def test_create_passenger(client):
#     response = client.post("/passenger/", json={"id": 10, "name": "Pepe", "phone_number": 55391608, "password": "12345"})
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "John Doe"
#     assert data["phone_number"] == "55193109"
#     assert data["password"] == "12345"
    

def test_get_passenger():
    db = override_get_db()
    client = TestClient(app)
    response = client.get("/passenger/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["phone_number"] == "55193109"
    assert data["password"] == "12345"


def test_get_passenger_by_phone_number():
    db = override_get_db()
    client = TestClient(app)
    response = client.get("/passenger/phone_number/55193109")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["phone_number"] == "55193109"
    assert data["password"] == "12345"


def test_get_all_passengers():
    db = override_get_db()
    client = TestClient(app)
    response = client.get("/passenger/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 4
    assert data[0]["name"] == PASSENGER_ONE["name"]
    assert data[0]["phone_number"] == PASSENGER_TWO["phone_number"]
    assert data[0]["password"] == PASSENGER_THREE["password"]
    assert data[1]["name"] == PASSENGER_TWO["name"]
    assert data[1]["phone_number"] == PASSENGER_TWO["phone_number"]
    assert data[1]["password"] == PASSENGER_TWO["password"]
    assert data[2]["name"] == PASSENGER_THREE["name"]
    assert data[2]["phone_number"] == PASSENGER_THREE["phone_number"]
    assert data[2]["password"] == PASSENGER_THREE["password"]
    assert data[3]["name"] == PASSENGER_FOUR["name"]
    assert data[3]["phone_number"] == PASSENGER_FOUR["phone_number"]
    assert data[3]["password"] == PASSENGER_FOUR["password"]


def test_delete_passenger():
    db = override_get_db()
    client = TestClient(app)
    response = client.delete("/passenger/1")
    assert response.status_code == 200
    get_response = client.get("/passenger/1")
    assert get_response.status_code == 404



