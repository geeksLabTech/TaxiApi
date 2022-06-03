from sqlalchemy.orm import Session
from models import PlaceDB, FamousPlacesDB
from schemas import FamousPlaces
from fastapi import Depends


def get_famousplace(place_id: int, db: Session ):
    return db.query(FamousPlacesDB).filter(FamousPlacesDB.id == place_id).first()


def get_all_famousplaces(db: Session ):
    return db.query(FamousPlacesDB).all()


def get_famousplaces_by_name(name: str, db: Session ):
    return db.query(FamousPlacesDB).filter(FamousPlacesDB.name == name).first()


def create_famousplace(famousplace: FamousPlaces, db: Session ):
    db_famousplace = FamousPlacesDB(
        name=famousplace.name, address=famousplace.address, latitude=famousplace.latitude, longitude=famousplace.longitude)
    db.add(db_famousplace)
    db.commit()
    db.refresh(db_famousplace)
    return db_famousplace


def update_famousplace (famousplace_id: int, name : str , address : str , latitude :str , longitude : str,db : Session):
    db_famousplace = db.query(FamousPlacesDB).filter(
        FamousPlacesDB.id == famousplace_id).first()
    db_famousplace.name = name
    db_famousplace.address = address
    db_famousplace.latitude = latitude
    db_famousplace.longitude = longitude
    db.commit()
    return db_famousplace


def delete_famousplace(famousplace_id: int, db: Session ):
    db_famousplace = db.query(FamousPlacesDB).filter(
        FamousPlacesDB.id == famousplace_id).first()
    db.delete(db_famousplace)
    db.commit()
    return db_famousplace
