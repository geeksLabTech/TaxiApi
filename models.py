
from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from tables import Col
from database import Base

DecBase = declarative_base()

table_driver_vehicle = Table(
    'driver_vehicle', Base.metadata,
    Column("driver_id", Integer, ForeignKey("driver.id"), nullable=True),
    Column("vehicle_id", Integer, ForeignKey("vehicle.id"), nullable=True),
    # __table_args__ = {'extend_existing': True}
    )


table_trip = Table(
    'trip', Base.metadata,
    Column("trip_id",Integer,ForeignKey("trip.id"),nullable = True),
    Column("driver_id", Integer, ForeignKey("driver.id"), nullable=True),
    Column("vehicle_id", Integer, ForeignKey("vehicle.id"), nullable=True),
    Column("passanger_id",Integer,ForeignKey("passanger.id"),nullable = True),
    # __table_args__ = {'extend_existing': True}
    )

class PassengerDB(Base):
    __tablename__ = 'passenger'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    phone_number = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    trips = relationship("TripDB", back_populates="passenger")


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
    brand = Column(String(64), nullable=False)
    color = Column(String(64), nullable=False)
    license_plate = Column(String(64), nullable=False)
    seats = Column(Integer, nullable=False)
    drivers = relationship(
        "DriverDB", secondary=table_driver_vehicle, backref="all_vehicles")
    model = Column(String(64), nullable=False)


class PlaceDB(Base):
    __tablename__ = 'places'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    address = Column(String(64), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    trips = relationship("TripDB", back_populates="destination")


class TripDB(Base):
    __tablename__ = 'trip'
    __table_args__ = {'extend_existing': True}
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
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, ForeignKey('places.id'), primary_key=True)
    description = Column(String(64), nullable=False)
    classification = Column(String(64), nullable=False)

