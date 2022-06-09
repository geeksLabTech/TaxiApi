from sqlalchemy.orm import Session
from models import VehicleBrandDB
from schemas import VehicleBrand
from fastapi import Depends


def get_brand_by_id(brand_id: int, db: Session ):
    return db.query(VehicleBrandDB).filter(VehicleBrandDB.id == brand_id).first()

def get_all_vehiclebrands(db: Session ):
    return db.query(VehicleBrandDB).all()


def get_vehiclebrand_by_name(name: str, db: Session ):
    return db.query(VehicleBrandDB).filter(VehicleBrandDB.name == name).first()


def create_vehiclebrand(vehiclebrand: VehicleBrand, db: Session ):
    db_vehiclebrand = VehicleBrandDB(
        name=vehiclebrand.name)
    db.add(db_vehiclebrand)
    db.commit()
    db.refresh(db_vehiclebrand)
    return db_vehiclebrand


def update_vehiclebrand (vehiclebrand_id: int, name : str, db : Session):
    db_vehiclebrand = db.query(VehicleBrandDB).filter(
        VehicleBrandDB.id == vehiclebrand_id).first()
    db_vehiclebrand.name = name
    db.commit()
    return db_vehiclebrand


def delete_vehiclebrand(vehiclebrand_id: int, db: Session ):
    db_vehiclebrand = db.query(VehicleBrandDB).filter(
        VehicleBrandDB.id == vehiclebrand_id).first()
    db.delete(db_vehiclebrand)
    db.commit()
    return db_vehiclebrand
