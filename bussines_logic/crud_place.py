from sqlalchemy.orm import Session

from models import PlaceDB
from schemas import Place


def get_place(place_id: int, db: Session):
    return db.query(PlaceDB).filter(PlaceDB.id == place_id).first()


def get_all_places(db: Session):
    return db.query(PlaceDB).all()


def get_place_by_name(name: str, db: Session):
    return db.query(PlaceDB).filter(PlaceDB.name == name).first()


def create_place(place: Place, db: Session):
    db_place = PlaceDB(
        name=place.name, address=place.address, latitude=place.latitude, longitude=place.longitude)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


def update_place( place_id: int,name : str , address : str , latitude : str , longitude : str ,db: Session):
    db_place = db.query(PlaceDB).filter(
        PlaceDB.id == place_id).first()
    db_place.name = name
    db_place.address = address
    db_place.latitude = latitude
    db_place.longitude = longitude
    db.commit()
    return db_place


def delete_place(place_id: int, db: Session):
    db_place = db.query(PlaceDB).filter(
        PlaceDB.id == place_id).first()
    db.delete(db_place)
    db.commit()
    return db_place
