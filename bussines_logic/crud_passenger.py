from sqlalchemy.orm import Session
from . import models, schemas


def get_passenger(db: Session, passenger_id: int):
    return db.query(models.Pasenger).filter(models.Pasenger.id == passenger_id).first()


def get_passenger_by_phone_number(db: Session, phone_number: str):
    return db.query(models.Pasenger).filter(models.Pasenger.phone_number == phone_number).first()


def get_passengers(db: Session):
    return db.query(models.Pasenger).all()


def create_passenger(db: Session, passenger: schemas.PasengerCreate):
    db_passenger = models.Pasenger(
        name=passenger.name, phone_number=passenger.phone_number, password=passenger.password)
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger


def update_passenger(db: Session, passenger_id: int, passenger: schemas.PasengerUpdate):
    db_passenger = db.query(models.Pasenger).filter(
        models.Pasenger.id == passenger_id).first()
    db_passenger.name = passenger.name
    db_passenger.phone_number = passenger.phone_number
    db_passenger.password = passenger.password
    db.commit()
    return db_passenger


def delete_passenger(db: Session, passenger_id: int):
    db_passenger = db.query(models.Pasenger).filter(
        models.Pasenger.id == passenger_id).first()
    db.delete(db_passenger)
    db.commit()
    return db_passenger
