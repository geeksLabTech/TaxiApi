
from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base

DecBase = declarative_base()

table_driver_vehicle = Table(
    'driver_vehicle', Base.metadata,
    Column("driver_id", Integer, ForeignKey("driver.id"), nullable=True),
    Column("vehicle_id", Integer, ForeignKey("vehicle.id"), nullable=True),
    # __table_args__ = {'extend_existing': True}
    )

class PassengerDB(Base):
    __tablename__ = 'passenger'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    trips = relationship("TripDB", backref="passenger")


class DriverDB(Base):
    __tablename__ = 'driver'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    ci = Column(String(64), nullable=False)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    vehicles = relationship(
        "VehicleDB", secondary=table_driver_vehicle, backref="all_drivers")


class VehicleDB(Base):
    __tablename__ = 'vehicle'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    color = Column(String(64), nullable=False)
    license_plate = Column(String(64), nullable=False)
    drivers = relationship(
        "DriverDB", secondary=table_driver_vehicle, backref="all_vehicles")
    trips = relationship("TripDB", backref="vehicle")
    model = Column(Integer, ForeignKey("vehicle_model.id"), nullable=False)


class PlaceDB(Base):
    __tablename__ = 'places'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=True)
    address = Column(String(64), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class TripDB(Base):
    __tablename__ = 'trip'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    time = Column(String(64), nullable=False)
    price = Column(Float, nullable=False)
    distance = Column(Float, nullable=False)
    status = Column(String(64), nullable=False)

    origin_id = Column(
        Integer, ForeignKey('places.id'), nullable=False)
    destination_id = Column(
        Integer, ForeignKey('places.id'), nullable=False)

    origin = relationship("PlaceDB", foreign_keys=[origin_id], uselist=False)
    destination = relationship("PlaceDB", foreign_keys=[destination_id], uselist=False)

    driver_id = Column(
        Integer, ForeignKey('driver.id'), nullable=False)
    vehicle_id = Column(
        Integer, ForeignKey('vehicle.id'), nullable=False)
    passenger_id = Column(
        Integer, ForeignKey('passenger.id'), nullable=False)



class FamousPlacesDB(PlaceDB):
    __tablename__ = 'famous_places'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, ForeignKey('places.id'), primary_key=True)
    description = Column(String(64), nullable=False)
    classification = Column(String(64), nullable=False)

class VehicleBrandDB(Base):
    __tablename__ = 'vehicle_brand'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    
class VehicleModelDB(Base):
    __tablename__ = 'vehicle_model'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey('vehicle_brand.id'), nullable=False)
    name = Column(String(64), nullable=False)
    seats = Column(Integer, nullable=False)