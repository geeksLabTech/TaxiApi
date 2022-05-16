from sqlalchemy.orm import Session
from . import models, schemas


def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()


def get_places(db: Session):
    return db.query(models.Place).all()


def get_places_by_name(db: Session, name: str):
    return db.query(models.Place).filter(models.Place.name == name).first()


def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(
        name=place.name, address=place.address, latitude=place.latitude, longitude=place.longitude)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


def update_place(db: Session, place_id: int, place: schemas.PlaceUpdate):
    db_place = db.query(models.Place).filter(
        models.Place.id == place_id).first()
    db_place.name = place.name
    db_place.address = place.address
    db_place.latitude = place.latitude
    db_place.longitude = place.longitude
    db.commit()
    return db_place


def delete_place(db: Session, place_id: int):
    db_place = db.query(models.Place).filter(
        models.Place.id == place_id).first()
    db.delete(db_place)
    db.commit()
    return db_place
