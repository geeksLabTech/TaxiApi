from sqlalchemy.orm import Session
from . import models, schemas


def get_drivervehicle(db: Session, driver_id: int, vehicle_id: int):
    return db.query(models.DriverVehicle).filter(models.DriverVehicle.driver_id == driver_id, models.DriverVehicle.vehicle_id == vehicle_id).first()


def get_drivervehicles(db: Session):
    return db.query(models.DriverVehicle).all()


def create_drivervehicle(db: Session, drivervehicle: schemas.DriverVehicleCreate):
    db_drivervehicle = models.DriverVehicle(
        driver_id=drivervehicle.driver_id, vehicle_id=drivervehicle.vehicle_id)
    db.add(db_drivervehicle)
    db.commit()
    db.refresh(db_drivervehicle)
    return db_drivervehicle


def update_drivervehicle(db: Session, driver_id: int, vehicle_id: int, drivervehicle: schemas.DriverVehicleUpdate):
    db_drivervehicle = db.query(models.DriverVehicle).filter(
        models.DriverVehicle.driver_id == driver_id, models.DriverVehicle.vehicle_id == vehicle_id).first()
    db_drivervehicle.driver_id = drivervehicle.driver_id
    db_drivervehicle.vehicle_id = drivervehicle.vehicle_id


def delete_drivervehicle(db: Session, driver_id: int, vehicle_id: int):
    db_drivervehicle = db.query(models.DriverVehicle).filter(
        models.DriverVehicle.driver_id == driver_id, models.DriverVehicle.vehicle_id == vehicle_id).first()
    db.delete(db_drivervehicle)
    db.commit()
    return db_drivervehicle
