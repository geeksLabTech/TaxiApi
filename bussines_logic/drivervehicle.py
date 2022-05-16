from sqlalchemy.orm import Session
from .. import models, schemas
from ..models import DriverVehicleDB


def get_drivervehicle(db: Session, driver_id: int, vehicle_id: int):
    return db.query(DriverVehicleDB).filter(DriverVehicleDB.driver_id == driver_id, DriverVehicleDB.vehicle_id == vehicle_id).first()


def get_drivervehicles(db: Session):
    return db.query(DriverVehicleDB).all()


def create_drivervehicle(db: Session, drivervehicle: DriverVehicleDB):
    db_drivervehicle = DriverVehicleDB(
        driver_id=drivervehicle.driver_id, vehicle_id=drivervehicle.vehicle_id)
    db.add(db_drivervehicle)
    db.commit()
    db.refresh(db_drivervehicle)
    return db_drivervehicle


# def update_drivervehicle(db: Session, driver_id: int, vehicle_id: int, drivervehicle: DriverVehicleDB):
#     db_drivervehicle = db.query(DriverVehicleDB).filter(
#         DriverVehicleDB.driver_id == driver_id, DriverVehicleDB.vehicle_id == vehicle_id).first()
#     db_drivervehicle.driver_id = drivervehicle.driver_id
#     db_drivervehicle.vehicle_id = drivervehicle.vehicle_id


def delete_drivervehicle(db: Session, driver_id: int, vehicle_id: int):
    db_drivervehicle = db.query(DriverVehicleDB).filter(
        DriverVehicleDB.driver_id == driver_id, DriverVehicleDB.vehicle_id == vehicle_id).first()
    db.delete(db_drivervehicle)
    db.commit()
    return db_drivervehicle
