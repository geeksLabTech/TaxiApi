from sqlalchemy.orm import Session
from . import models, schemas


def get_driver(db: Session, driver_id: int):
    return db.query(models.Driver).filter(models.Driver.id == driver_id).first()


def get_driver_by_ci(db: Session, ci: str):
    return db.query(models.Driver).filter(models.Driver.ci == ci).first()


def get_driver_by_phone_number(db: Session, phone_number: str):
    return db.query(models.Driver).filter(models.Driver.phone_number == phone_number).first()


def get_drivers(db: Session):
    return db.query(models.Driver).all()


def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(ci=driver.ci, name=driver.name,
                              phone_number=driver.phone_number, password=driver.password)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def update_driver(db: Session, driver_id: int, driver: schemas.DriverUpdate):
    db_driver = db.query(models.Driver).filter(
        models.Driver.id == driver_id).first()
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
