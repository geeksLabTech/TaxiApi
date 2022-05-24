from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base


class PassengerDB(Base):
    __tablename__ = 'passenger'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    trips = relationship("TripDB", back_populates="passenger")


class DriverDB(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True, index=True)
    ci = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    vehicle = relationship("VehicleDB", back_populates="driver")


class VehicleDB(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    brand = Column(String(64), nullable=False)
    color = Column(String(64), nullable=False)
    license_plate = Column(String(64), nullable=False)
    seats = Column(Integer, nullable=False)
    driver_id = Column(Integer, ForeignKey('driver.id'), nullable=False)
    # driver = relationship("DriverDB", back_populates="vhicles?")
    driver = relationship("DriverDB", back_populates="vehicle")
    model = Column(String(64), nullable=False)


class DriverVehicleDB(Base):
    __tablename__ = 'driver_vehicle'
    driver_id = Column(Integer, ForeignKey('driver.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


class PlaceDB(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    address = Column(String(64), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    trips = relationship("TripDB", back_populates="destination")


class TripDB(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    time = Column(String(64), nullable=False)
    price = Column(Float, nullable=False)
    distance = Column(Float, nullable=False)
    origin = Column(Integer, ForeignKey('places.id'), nullable=False)
    status = Column(String(64), nullable=False)
    destination = relationship("PlaceDB", back_populates='trips')
    driver_id = Column(
        Integer, ForeignKey('driver.id'), nullable=False)
    vehicle_id = Column(
        Integer, ForeignKey('vehicle.id'), nullable=False)
    passenger_id = Column(Integer, ForeignKey('passenger.id'), nullable=False)
    passenger = relationship('PassengerDB', back_populates='trips')


class FamousPlacesDB(PlaceDB):
    __tablename__ = 'famous_places'
    id = Column(Integer, ForeignKey('places.id'), primary_key=True)
    description = Column(String(64), nullable=False)
    classification = Column(String(64), nullable=False)
