from sqlalchemy.orm import Session
from models import PassengerDB
from schemas import Passenger


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


# def update_passenger(db: Session, passenger_id: int, passenger: schemas.PasengerUpdate):
#     db_passenger = db.query(PassengerDB).filter(
#         PassengerDB.id == passenger_id).first()
#     db_passenger.name = passenger.name
#     db_passenger.phone_number = passenger.phone_number
#     db_passenger.password = passenger.password
#     db.commit()
#     return db_passenger


def delete_passenger(passenger_id: int, db: Session ):
    db_passenger = db.query(PassengerDB).filter(
        PassengerDB.id == passenger_id).first()
    db.delete(db_passenger)
    db.commit()
    return db_passenger
