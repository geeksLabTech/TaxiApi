from sqlalchemy.orm import Session
from models import PassengerDB
from schemas import Passenger
import schemas

def get_passenger(passenger_id: int, db: Session ):
    return db.query(PassengerDB).filter(PassengerDB.id == passenger_id).first()


def get_passenger_by_phone_number(phone_number: str, db: Session ):
    return db.query(PassengerDB).filter(PassengerDB.phone_number == phone_number).first()

def get_all_passengers(db: Session ):
    return db.query(PassengerDB).all()


def create_passenger(passenger: Passenger, db: Session ):
    db_passenger = PassengerDB(
        name=passenger.name, phone_number=passenger.phone_number, password=passenger.password)
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger


def update_passenger(passenger_id: int,name : str , phone_number:str, password : str,db:Session):
    db_passenger = db.query(PassengerDB).filter(
        PassengerDB.id == passenger_id).first()
    db_passenger.name = name
    db_passenger.phone_number = phone_number
    db_passenger.password = password
    db.commit()
    return db_passenger


def delete_passenger(passenger_id: int, db: Session ):
    db_passenger = db.query(PassengerDB).filter(
        PassengerDB.id == passenger_id).first()
    db.delete(db_passenger)
    db.commit()
    return db_passenger
