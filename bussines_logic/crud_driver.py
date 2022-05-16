from sqlalchemy.orm import Session
from .. import models, schemas
from typing import Union


def get_driver(db: Session, driver_id: int):
    return db.query(models.DriverDB).filter(models.DriverDB.id == driver_id).first()


def get_driver_by_ci(db: Session, ci: str):
    return db.query(models.DriverDB).filter(models.DriverDB.ci == ci).first()


def get_driver_by_phone_number(db: Session, phone_number: str):
    return db.query(models.DriverDB).filter(models.DriverDB.phone_number == phone_number).first()


def get_drivers(db: Session):
    return db.query(models.DriverDB).all()


def create_driver(db: Session, driver: schemas.Driver):
    db_driver = models.DriverDB(ci=driver.ci, name=driver.name,
                              phone_number=driver.phone_number, password=driver.password)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def update_driver(db: Session, driver_id: int, driver: schemas.Driver):
    db_driver: Union[models.DriverDB, None] = db.query(models.DriverDB).filter(
        models.DriverDB.id == driver_id).first()
    db_driver.name = driver.name
    db_driver.phone_number = driver.phone_number
    db_driver.password = driver.password
    db.commit()
    return db_driver


def delete_driver(db: Session, driver_id: int):
    db_driver = db.query(models.Driver).filter(
        models.Driver.id == driver_id).first()
    db.delete(db_driver)
    db.commit()
    return db_driver
