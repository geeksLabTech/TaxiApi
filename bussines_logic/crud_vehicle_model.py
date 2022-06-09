from sqlalchemy.orm import Session
from models import VehicleModelDB
from schemas import VehicleModel
from fastapi import Depends


def get_model_by_id(model_id: int, db: Session ):
    return db.query(VehicleModelDB).filter(VehicleModelDB.id == model_id).first()

def get_all_vehiclemodels(db: Session ):
    return db.query(VehicleModelDB).all()

def get_models_by_brand(brand_id: int, db: Session ):
    return db.query(VehicleModelDB).filter(VehicleModelDB.brand_id == brand_id).all()

def get_vehiclemodel_by_name(name: str, db: Session ):
    return db.query(VehicleModelDB).filter(VehicleModelDB.name == name).first()

def create_vehiclemodel(vehiclemodel: VehicleModel, db: Session ):
    db_vehiclemodel = VehicleModelDB(
        name=vehiclemodel.name, brand_id=vehiclemodel.brand_id, seats=vehiclemodel.seats)
    db.add(db_vehiclemodel)
    db.commit()
    db.refresh(db_vehiclemodel)
    return db_vehiclemodel


def update_vehiclemodel (vehiclemodel_id: int, name : str, db : Session):
    db_vehiclemodel = db.query(VehicleModelDB).filter(
        VehicleModelDB.id == vehiclemodel_id).first()
    db_vehiclemodel.name = name
    db.commit()
    return db_vehiclemodel


def delete_vehiclemodel(vehiclemodel_id: int, db: Session ):
    db_vehiclemodel = db.query(VehicleModelDB).filter(
        VehicleModelDB.id == vehiclemodel_id).first()
    db.delete(db_vehiclemodel)
    db.commit()
    return db_vehiclemodel
