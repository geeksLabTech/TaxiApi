from fastapi import APIRouter, Depends, HTTPException
from ..schemas import DriverVehicle
from typing import List
from sqlalchemy.orm import Session
from ..bussines_logic import crud_drivervehicle
from ..dependencies import get_db


router = APIRouter(
    prefix="/drivervehicle",
    tags=["DriverVehicle"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[DriverVehicle])
def get_all_drivervehicles(db: Session = Depends(get_db)):
    return crud_drivervehicle.get_all_drivervehicles(db)


@router.get("/{drivervehicle_id}", response_model=DriverVehicle)
def get_drivervehicle(driver_id: int, vehicle_id, db: Session = Depends(get_db)):
    drivervehicle = crud_drivervehicle.get_drivervehicle(driver_id, vehicle_id, db)
    if not drivervehicle:
        raise HTTPException(status_code=404, detail="DriverVehicle not found")
    return drivervehicle


@router.post("/", response_model=DriverVehicle)
def create_drivervehicle(drivervehicle: DriverVehicle, db: Session = Depends(get_db)):
    return crud_drivervehicle.create_drivervehicle(drivervehicle, db)


@router.delete("/{driver_id}/{vehicle_id}", response_model=DriverVehicle)
def delete_drivervehicle(driver_id: int, vehicle_id: int, db: Session = Depends(get_db)):
    return crud_drivervehicle.delete_drivervehicle(driver_id, vehicle_id, db)