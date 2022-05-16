from sqlalchemy.orm import Session
from . import models, schemas


def get_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int):
    return db.query(models.Trip).filter(models.Trip.driver_id == driver_id, models.Trip.pasenger_id == pasenger_id, models.Trip.vehicle_id == vehicle_id).first()


def get_trips(db: Session):
    return db.query(models.Trip).all()


def create_trip(db: Session, trip: schemas.TripCreate):
    db_trip = models.Trip(driver_id=trip.driver_id,
                          pasenger_id=trip.pasenger_id, vehicle_id=trip.vehicle_id)
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip


def update_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int, trip: schemas.TripUpdate):
    db_trip = db.query(models.Trip).filter(models.Trip.driver_id == driver_id,
                                           models.Trip.pasenger_id == pasenger_id, models.Trip.vehicle_id == vehicle_id).first()
    db_trip.driver_id = trip.driver_id
    db_trip.pasenger_id = trip.pasenger_id
    db_trip.vehicle_id = trip.vehicle_id
    db.commit()


def delete_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int):
    db_trip = db.query(models.Trip).filter(models.Trip.driver_id == driver_id,
                                           models.Trip.pasenger_id == pasenger_id, models.Trip.vehicle_id == vehicle_id).first()
    db.delete(db_trip)
    db.commit()
    return db_trip
