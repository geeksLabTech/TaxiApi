from fastapi import APIRouter, Depends, HTTPException
from schemas import Passenger
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_passenger
from dependencies import get_db

router = APIRouter(
    prefix="/passenger",
    tags=["Passenger"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Passenger])
def get_all_passengers(db: Session = Depends(get_db)):
    return crud_passenger.get_all_passengers(db)


@router.get("/{passenger_id}", response_model=Passenger)
def get_passenger(passenger_id: int):
    passenger = crud_passenger.get_passenger(passenger_id)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger


@router.get("/phone_number/{phone_number}", response_model=Passenger)
def get_passenger_by_phone_number(phone_number: str):
    passenger = crud_passenger.get_passenger_by_phone_number(phone_number)
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger


@router.post("/", response_model=Passenger)
def create_passenger(passenger: Passenger):
    return crud_passenger.create_passenger(passenger)


@router.delete("/{passenger_id}", response_model=Passenger)
def delete_passenger(passenger_id: int):
    return crud_passenger.delete_passenger(passenger_id)