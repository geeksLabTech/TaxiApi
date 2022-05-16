from pydantic import BaseModel

# Class User with id, name, email, password


class Pasenger(BaseModel):
    id: int
    name: str
    phone_number: str
    password: str


class Drive(BaseModel):
    id: int
    ci: str
    name: str
    phone_number: str
    password: str


class Vehicle(BaseModel):
    id: int
    name: str
    brand: str
    color: str
    license_plate: str
    seats: int

    drive_id: int


class Place(BaseModel):
    id: int
    name: str
    address: str
    latitude: float
    longitude: float


class Trip(BaseModel):
    date: str
    time: str
    price: float
    distance: float
    origin: int
    destination: int
    drive_id: int
    pasenger_id: int
    vehicle_id: int
    status: str


class Famosus_Places(BaseModel, Place):
    description: str
    clasification: str
