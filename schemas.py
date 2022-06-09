from pydantic import BaseModel
from enum import Enum
# Class User with id, name, email, password


class Passenger(BaseModel):
    id: int
    name: str
    phone_number: str
    password: str

    class Config:
        orm_mode = True


class Driver(BaseModel):
    id: int
    ci: str
    name: str
    phone_number: str
    password: str

    class Config:
        orm_mode = True


class Vehicle(BaseModel):
    id: int
    name: str
    color: str
    license_plate: str
    model: str

    class Config:
        orm_mode = True


class DriverVehicle(BaseModel):
    driver_id: int
    vehicle_id: int

    class Config:
        orm_mode = True


class Place(BaseModel):
    id: int
    name: str
    address: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class Status(str, Enum):
    ACCEPTED              = 'ACCEPTED'
    REJECTED_BY_PASSENGER = 'REJECTED_BY_PASSENGER'
    REJECTED_BY_DRIVER    = 'REJECTED_BY_DRIVER'
    CANCELED              = 'CANCELED'
    FINISHED              = 'FINISHED'


class Trip(BaseModel):
    id: int
    date: str
    time: str
    price: float
    distance: float
    origin_id: int
    destination_id: int
    driver_id: int
    passenger_id: int
    vehicle_id: int
    status: Status

    class Config:
        orm_mode = True


class FamousPlaces(Place):
    description: str
    clasification: str

class VehicleBrand(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class VehicleModel(BaseModel):
    id: int
    brand_id: int
    name: str
    seats: int
    class Config:
        orm_mode = True