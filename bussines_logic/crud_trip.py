from sqlalchemy.orm import Session
import models
from models import table_trip
from routers import trip_route
from schemas import DriverVehicle, Trip
from schemas import Passenger


def get_trip(driver_id: int, pasenger_id: int, vehicle_id: int, db: Session):
    return db.query(table_trip).filter(table_trip.driver_id == driver_id, table_trip.pasenger_id == pasenger_id, table_trip.vehicle_id == vehicle_id).first()


def get_all_trips(db: Session):
    return db.query(table_trip).all()


def create_trip(trip: Trip, db: Session):
    driver = db.query(models.DriverDB).filter(models.DriverDB.id == trip.driver_id).first()
    vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == trip.vehicle_id).first()
    passanger = db.query(models.PassengerDB).filter(models.PassengerDB.id == trip.passnger_id).first()
    try:
        driver.vehicles.append(vehicle)
        vehicle.passanger.append(passanger)
        db.commit()
        return trip
    except:
        return "Somethig went wrong"


# def update_trip(db: Session, driver_id: int, pasenger_id: int, vehicle_id: int, trip: table_trip):
#     db_trip = db.query(table_trip).filter(table_trip.driver_id == driver_id,
#                                       table_trip.pasenger_id == pasenger_id, table_trip.vehicle_id == vehicle_id).first()
#     db_trip.driver_id = trip.driver_id
#     db_trip.pasenger_id = trip.pasenger_id
#     db_trip.vehicle_id = trip.vehicle_id
#     db.commit()


def delete_trip(driver_id: int, pasenger_id: int, vehicle_id: int, db: Session):
    db_trip = db.query(table_trip).filter(table_trip.driver_id == driver_id,
                                      table_trip.pasenger_id == pasenger_id, table_trip.vehicle_id == vehicle_id).first()
    db.delete(db_trip)
    db.commit()
    return db_trip
