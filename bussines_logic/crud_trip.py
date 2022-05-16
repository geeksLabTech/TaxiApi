from sqlalchemy.orm import Session
from .. import schemas
from ..models import TripDB
from ..schemas import Trip
from fastapi import Depends
from dependencies import get_deb


def get_trip(driver_id: int, pasenger_id: int, vehicle_id: int, db: Session = Depends(get_db)):
    return db.query(TripDB).filter(TripDB.driver_id == driver_id, TripDB.pasenger_id == pasenger_id, TripDB.vehicle_id == vehicle_id).first()


def get_trips(db: Session = Depends(get_db)):
    return db.query(TripDB).all()


def create_trip(trip: Trip, db: Session = Depends(get_db)):
    db_trip = TripDB(driver_id=trip.driver_id,
                     pasenger_id=trip.pasenger_id, vehicle_id=trip.vehicle_id)
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


# def update_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int, trip: TripDB):
#     db_trip = db.query(TripDB).filter(TripDB.driver_id == driver_id,
#                                       TripDB.pasenger_id == pasenger_id, TripDB.vehicle_id == vehicle_id).first()
#     db_trip.driver_id = trip.driver_id
#     db_trip.pasenger_id = trip.pasenger_id
#     db_trip.vehicle_id = trip.vehicle_id
#     db.commit()


def delete_trip(driver_id: int, pasenger_id: int, vehicle_id: int, db: Session = Depends(get_db)):
    db_trip = db.query(TripDB).filter(TripDB.driver_id == driver_id,
                                      TripDB.pasenger_id == pasenger_id, TripDB.vehicle_id == vehicle_id).first()
    db.delete(db_trip)
    db.commit()
    return db_trip
