from sqlalchemy.orm import Session
from . import schemas
from models import TripDB


def get_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int):
    return db.query(TripDB).filter(TripDB.driver_id == driver_id, TripDB.pasenger_id == pasenger_id, TripDB.vehicle_id == vehicle_id).first()


def get_trips(db: Session):
    return db.query(TripDB).all()


def create_trip(db: Session, trip: TripDB):
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


def delete_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int):
    db_trip = db.query(TripDB).filter(TripDB.driver_id == driver_id,
                                      TripDB.pasenger_id == pasenger_id, TripDB.vehicle_id == vehicle_id).first()
    db.delete(db_trip)
    db.commit()
    return db_trip
