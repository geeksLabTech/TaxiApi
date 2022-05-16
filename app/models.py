from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class PasengerDB(Base):
    __tablename__ = 'passeger'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    trips = relationship("TripDB", back_populates="pasenger")


class DriverDB(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True, index=True)
    ci = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    trips = relationship("VehicleDB", back_populates="driver")


class VehicleDB(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    brand = Column(String(64), nullable=False)
    color = Column(String(64), nullable=False)
    license_plate = Column(String(64), nullable=False)
    seats = Column(Integer, nullable=False)
    drive_id = Column(Integer, ForeignKey('driver.id'), nullable=False)
    trips = relationship("DriverDB", back_populates="vehicle")


class DriverVehicleDB(Base):
    __tablename__ = 'driver_vehicle'
    driver_id = Column(Integer, ForeignKey('driver.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)


class PlacesDB(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    address = Column(String(64), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    trips = relationship("TripDB", back_populates="origin")


class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    time = Column(String(64), nullable=False)
    price = Column(Float, nullable=False)
    distance = Column(Float, nullable=False)
    origin = Column(Integer, ForeignKey('places.id'), nullable=False)
    destination = Column(Integer, ForeignKey('places.id'), nullable=False)
    driver_vehicle_id = Column(
        Integer, ForeignKey('driver.id'), nullable=False)
    pasenger_id = Column(Integer, ForeignKey('passeger.id'), nullable=False)


class FamousPlacesDB(PlacesDB, Base):
    __tablename__ = 'famous_places'
    description = Column(String(64), nullable=False)
    clasification = Column(String(64), nullable=False)
