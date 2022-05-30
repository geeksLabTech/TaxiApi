from sqlalchemy.orm import Session
import schemas
from models import PlaceDB, FamousPlacesDB
from schemas import FamousPlaces
from fastapi import Depends


def get_famousplace(place_id: int, db: Session ):
    return db.query(PlaceDB).filter(PlaceDB.id == place_id).first()


def get_all_famousplaces(db: Session ):
    return db.query(PlaceDB).all()


def get_famousplaces_by_name(name: str, db: Session ):
    return db.query(PlaceDB).filter(PlaceDB.name == name).first()


def create_famousplace(place: FamousPlaces, db: Session ):
    db_place = PlaceDB(
        name=place.name, address=place.address, latitude=place.latitude, longitude=place.longitude)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


# def update_famousplace(db: Session, place_id: int, place: schemas.PlaceUpdate):
#     db_place = db.query(PlaceDB).filter(
#         PlaceDB.id == place_id).first()
#     db_place.name = place.name
#     db_place.address = place.address
#     db_place.latitude = place.latitude
#     db_place.longitude = place.longitude
#     db.commit()
#     return db_place


def delete_famousplace(place_id: int, db: Session ):
    db_place = db.query(PlaceDB).filter(
        PlaceDB.id == place_id).first()
    db.delete(db_place)
    db.commit()
    return db_place
