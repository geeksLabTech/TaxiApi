from sqlalchemy.orm import Session

from .models import VehicleDB
from .schemas import Vehicle

def get_vehicle(vehicle_id: int, db: Session ):
    return db.query(VehicleDB).filter(VehicleDB.id == vehicle_id).first()


def get_vehicles(db: Session ):
    return db.query(VehicleDB).all()


def create_vehicle(vehicle: Vehicle, db: Session ):
    db_vehicle = VehicleDB(license_plate=vehicle.license_plate, brand=vehicle.brand,
                           model=vehicle.model, color=vehicle.color , driver_id=vehicle.driver_id)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


# def update_vehicle(db: Session, vehicle_id: int, vehicle: VehicleDB):
#     db_vehicle = db.query(VehicleDB).filter(
#         VehicleDB.id == vehicle_id).first()
#     db_vehicle.license_plate = vehicle.license_plate
#     db_vehicle.brand = vehicle.brand
#     db_vehicle.model = vehicle.model
#     db_vehicle.color = vehicle.color
#     db_vehicle.year = vehicle.year
#     db_vehicle.driver_id = vehicle.driver_id
#     db.commit()
#     return db_vehicle


def delete_vehicle(vehicle_id: int, db: Session ):
    db_vehicle = db.query(VehicleDB).filter(
        VehicleDB.id == vehicle_id).first()
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle


def get_vehicle_by_license_plate(license_plate: str, db: Session ):
    return db.query(VehicleDB).filter(VehicleDB.license_plate == license_plate).first()
