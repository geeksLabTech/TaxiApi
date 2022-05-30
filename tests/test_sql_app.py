
from typing import Iterable
import pytest

#from test_main import client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .test_data.test_driver_data import DRIVERS_DB
from .test_data.test_driver_vechicle_data import DRIVERS_VEHICLES_DB
from .test_data.test_famousplaces_data import FAMOUS_PLACES_DB

from .test_data.test_passenger_data import PASSENGERS_DB
from .test_data.test_place_data import PLACES_DB
from .test_data.test_trip_data import TRIPS_DB
from .test_data.test_vehicle_data import VECHICLES_DB

from ..database import Base
from fastapi.testclient import TestClient
from ..main import app
from ..dependencies import get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def populate_test_db_with_fake_data(db):
    data_to_add = []
    for passenger in PASSENGERS_DB:
        data_to_add.append(passenger)
    for driver in DRIVERS_DB:
        data_to_add.append(driver)
    for vehicle in VECHICLES_DB:
        data_to_add.append(vehicle)
    for place in PLACES_DB:
        data_to_add.append(place)
    for trip in TRIPS_DB:
        data_to_add.append(trip)
    for drivervehicle in DRIVERS_VEHICLES_DB:
        data_to_add.append(drivervehicle)
    for famous in FAMOUS_PLACES_DB:
        data_to_add.append(famous)
        
    
    db.add_all(data_to_add)
    
    db.commit()



@pytest.fixture()
def session():
    
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    populate_test_db_with_fake_data(db)

    try:
        yield db
    finally:
        db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client(session) -> Iterable[TestClient]:

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


