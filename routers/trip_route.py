from fastapi import APIRouter, Depends, HTTPException
from schemas import Trip
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_trip
from dependencies import get_db


router = APIRouter(
    prefix="/trip",
    tags=["Trip"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_all_trips(db: Session = Depends(get_db)):
    return crud_trip.get_all_trips(db)


router.get("/{trip_id}")
def get_trip(trip_id: int, pasenger_id: int, vehicle_id: int, db: Session = Depends(get_db)):
    trip = crud_trip.get_trip(trip_id, pasenger_id, vehicle_id, db)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip


@router.post("/")
def create_trip(trip: Trip, db: Session = Depends(get_db)):
    return crud_trip.create_trip(trip, db)


@router.delete("/{trip_id}")
def delete_trip(trip_id: int, pasenger_id: int, vehicle_id: int, db: Session = Depends(get_db)):
    return crud_trip.delete_trip(trip_id, pasenger_id, vehicle_id, db)