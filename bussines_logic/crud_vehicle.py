from sqlalchemy.orm import Session

from models import VehicleDB
from schemas import Vehicle


def get_vehicle(vehicle_id: int, db: Session):
    return db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()


def get_all_vehicles(db: Session):
    return db.query(VehicleDB).all()


def create_vehicle(vehicle: Vehicle, db: Session):
    db_vehicle = VehicleDB(name=vehicle.name,license_plate=vehicle.license_plate,model=vehicle.model, color=vehicle.color)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def update_vehicle(vehicle_id: int, name:str, license_plate : str, model : str ,color : str ,db: Session):
    db_vehicle = db.query(VehicleDB).filter(
        VehicleDB.id == vehicle_id).first()
    db_vehicle.license_plate = license_plate
    db_vehicle.model = model
    db_vehicle.name = name
    db_vehicle.color = color
    db_vehicle.driver_id = vehicle_id
    db.commit()
    return db_vehicle


def delete_vehicle(vehicle_id: int, db: Session):
    db_vehicle = db.query(VehicleDB).filter(
        VehicleDB.id == vehicle_id).first()
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle


def get_vehicle_by_license_plate(license_plate: str, db: Session):
    return db.query(VehicleDB).filter(VehicleDB.license_plate == license_plate).first()
