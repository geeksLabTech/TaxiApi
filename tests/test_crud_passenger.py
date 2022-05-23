from .test_sql_app import client

def test_create_passenger():
    response = client.post("/passenger/", json={"name": "John Doe", "phone_number": 55193109, "password": "12345"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["phone_number"] == 55193109
    assert data["password"] == "12345"
    

def test_get_passenger():
    response = client.get("/passenger/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["phone_number"] == 55193109
    assert data["password"] == "12345"


def test_get_passenger_by_phone_number():
    response = client.get("/passenger/phone_number/55193109")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["phone_number"] == 55193109
    assert data["password"] == "12345"


def test_get_all_passengers():
    response = client.get("/passenger/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "John Doe"
    assert data[0]["phone_number"] == 55193109
    assert data[0]["password"] == "12345"



