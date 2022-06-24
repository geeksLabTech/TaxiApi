from fastapi import APIRouter, Depends, HTTPException
from schemas import Vehicle
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_vehicle
from dependencies import get_db

router = APIRouter(
    prefix="/vehicle",
    tags=["Vehicle"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Vehicle])
def get_all_vehicles(db: Session = Depends(get_db)):
    return crud_vehicle.get_all_vehicles(db)


@router.get("/{vehicle_id}", response_model=Vehicle)
def get_vehicle(vehicle_id: int, db: Session = Depends(get_db)):   
    vehicle = crud_vehicle.get_vehicle(vehicle_id, db)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.get("/lincense_plate/{license_plate}",response_model= Vehicle)
def get_vehicle_for_lincense_plate(license_plate:str, db :Session = Depends(get_db)):
    return crud_vehicle.get_vehicle_by_license_plate(license_plate,db)


@router.post("/", response_model=Vehicle)
def create_vehicle(vehicle: Vehicle, db: Session = Depends(get_db)):
    if(crud_vehicle.get_vehicle_by_license_plate(vehicle.license_plate,db) is not None):
         raise HTTPException(status_code=409, detail="There is already a vehicle with this license plate")
    return crud_vehicle.create_vehicle(vehicle, db)

@router.put("/{vehicle_id}",response_model=Vehicle)
def update_vehicle(vehicle_id: int, name: str, license_plate : str, model : str ,color : str  ,db: Session=Depends(get_db)):
    return crud_vehicle.update_vehicle(vehicle_id,name, license_plate , model ,color ,db)


@router.delete("/{vehicle_id}", response_model=Vehicle)
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    return crud_vehicle.delete_vehicle(vehicle_id, db)
