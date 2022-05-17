from sqlalchemy.orm import Session
from .. import schemas
from ..models import PlaceDB, FamousPlacesDB


def get_famousplace(db: Session, place_id: int):
    return db.query(PlaceDB).filter(PlaceDB.id == place_id).first()


def get_famousplaces(db: Session):
    return db.query(PlaceDB).all()


def get_famousplaces_by_name(db: Session, name: str):
    return db.query(PlaceDB).filter(PlaceDB.name == name).first()


def create_famousplace(db: Session, place: FamousPlacesDB):
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


def delete_famousplace(db: Session, place_id: int):
    db_place = db.query(PlaceDB).filter(
        PlaceDB.id == place_id).first()
    db.delete(db_place)
    db.commit()
    return db_place