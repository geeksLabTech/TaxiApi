from sqlalchemy.orm import Session
from . import models, schemas


def get_vehicle(db: Session, vehicle_id: int):
    return db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()


def get_vehicles(db: Session):
    return db.query(models.Vehicle).all()


def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    db_vehicle = models.Vehicle(license_plate=vehicle.license_plate, brand=vehicle.brand,
                                model=vehicle.model, color=vehicle.color, year=vehicle.year, driver_id=vehicle.driver_id)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def update_vehicle(db: Session, vehicle_id: int, vehicle: schemas.VehicleUpdate):
    db_vehicle = db.query(models.Vehicle).filter(
        models.Vehicle.id == vehicle_id).first()
    db_vehicle.license_plate = vehicle.license_plate
    db_vehicle.brand = vehicle.brand
    db_vehicle.model = vehicle.model
    db_vehicle.color = vehicle.color
    db_vehicle.year = vehicle.year
    db_vehicle.driver_id = vehicle.driver_id
    db.commit()
    return db_vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(models.Vehicle).filter(
        models.Vehicle.id == vehicle_id).first()
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle


def get_vehicle_by_license_plate(db: Session, license_plate: str):
    return db.query(models.Vehicle).filter(models.Vehicle.license_plate == license_plate).first()
