from sqlalchemy.orm import Session
from .. import schemas
from ..models import PassengerDB
from fastapi import Depends
from dependencies import get_db



def get_passenger( passenger_id: int, db: Session = Depends(get_db)):
    return db.query(PassengerDB).filter(PassengerDB.id == passenger_id).first()


def get_passenger_by_phone_number(phone_number: str, db: Session = Depends(get_db)):
    return db.query(PassengerDB).filter(PassengerDB.phone_number == phone_number).first()


def get_passengers(db: Session = Depends(get_db)):
    return db.query(PassengerDB).all()


def create_passenger(passenger: PassengerDB, db: Session = Depends(get_db)):
    db_passenger = PassengerDB(
        name=passenger.name, phone_number=passenger.phone_number, password=passenger.password)
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger


# def update_passenger(db: Session, passenger_id: int, passenger: schemas.PasengerUpdate):
#     db_passenger = db.query(PassengerDB).filter(
#         PassengerDB.id == passenger_id).first()
#     db_passenger.name = passenger.name
#     db_passenger.phone_number = passenger.phone_number
#     db_passenger.password = passenger.password
#     db.commit()
#     return db_passenger


def delete_passenger(passenger_id: int, db: Session = Depends(get_db)):
    db_passenger = db.query(PassengerDB).filter(
        PassengerDB.id == passenger_id).first()
    db.delete(db_passenger)
    db.commit()
    return db_passenger
