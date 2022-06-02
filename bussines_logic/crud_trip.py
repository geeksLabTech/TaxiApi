from turtle import distance
from sqlalchemy.orm import Session
import models
from models import TripDB
from routers import trip_route
from schemas import DriverVehicle, Trip
from schemas import Passenger


def get_trip(driver_id: int, passenger_id: int, vehicle_id: int, db: Session):
    return db.query(TripDB).filter(TripDB.driver_id == driver_id, TripDB.passenger_id == passenger_id, TripDB.vehicle_id == vehicle_id).first()


def get_all_trips(db: Session):
    return db.query(TripDB).all()


def create_trip(trip: Trip, db: Session):
    print("/n/n/n/n/n/n")
    origin = db.query(models.PlaceDB).filter(models.PlaceDB.id == trip.origin_id).first()
    print(origin)
    destination = db.query(models.PlaceDB).filter(models.PlaceDB.id == trip.destination_id).first()
    db_trip = TripDB(
        id=trip.id,
        date=trip.date, time=trip.time, price=trip.price, distance=trip.distance, origin_id=trip.origin_id, destination_id=trip.destination_id,
        status=trip.status, driver_id=trip.driver_id, passenger_id=trip.passenger_id, vehicle_id=trip.vehicle_id)

    try:
        db.add(db_trip)
        db.commit()
        db.refresh(db_trip)
        return db_trip

    except:
        return "Somethig went wrong"


# def update_trip(db: Session, driver_id: int, passenger_id: int, vehicle_id: int, trip: TripDB):
#     db_trip = db.query(TripDB).filter(TripDB.driver_id == driver_id,
#                                       TripDB.passenger_id == passenger_id, TripDB.vehicle_id == vehicle_id).first()
#     db_trip.driver_id = trip.driver_id
#     db_trip.passenger_id = trip.passenger_id
#     db_trip.vehicle_id = trip.vehicle_id
#     db.commit()


def delete_trip(driver_id: int, passenger_id: int, vehicle_id: int, db: Session):
    db_trip = db.query(TripDB).filter(TripDB.driver_id == driver_id,
                                      TripDB.passenger_id == passenger_id, TripDB.vehicle_id == vehicle_id).first()
    db.delete(db_trip)
    db.commit()
    return db_trip
