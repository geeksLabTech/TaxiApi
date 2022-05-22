from fastapi import APIRouter, Depends, HTTPException
from schemas import Driver
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_driver
from dependencies import get_db


router = APIRouter(
    prefix="/driver",
    tags=["Driver"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Driver])
def get_all_drivers(db: Session = Depends(get_db)):
    return crud_driver.get_all_drivers(db)

@router.get("/{driver_id}", response_model=Driver)
def get_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud_driver.get_driver(driver_id, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.get("/phone_number/{phone_number}", response_model=Driver)
def get_driver_by_phone_number(phone_number: str, db: Session = Depends(get_db)):
    driver = crud_driver.get_driver_by_phone_number(phone_number, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.get("/ci/{ci}", response_model=Driver)
def get_driver_by_ci(ci: str, db: Session = Depends(get_db)):
    driver = crud_driver.get_driver_by_ci(ci, db)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.post("/", response_model=Driver)
def create_driver(driver: Driver, db: Session = Depends(get_db)):
    if db.query(crud_driver.get_driver_by_phone_number(driver.phone_number, db)).first() is not None:
        raise HTTPException(status_code=409, detail="Driver already exists")
    return crud_driver.create_driver(driver, db)


@router.delete("/{driver_id}", response_model=Driver)
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    if db.query(crud_driver.get_driver(driver_id, db)).first() is None:
        raise HTTPException(status_code=404, detail="Driver not found")

    return crud_driver.delete_driver(driver_id, db)
