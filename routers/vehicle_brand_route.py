from fastapi import APIRouter, Depends, HTTPException
from schemas import VehicleBrand
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_vehicle_brand
from dependencies import get_db


router = APIRouter(
    prefix="/vehiclebrand",
    tags=["Vehiclebrand"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[VehicleBrand])
def get_all_vehiclebrands(db: Session = Depends(get_db)):
    return crud_vehicle_brand.get_all_vehiclebrands(db)


@router.get("/{vehiclebrand_id}", response_model=VehicleBrand)
def get_vehiclebrands(vehiclebrand_id: int, db: Session = Depends(get_db)):
    vehiclebrand = crud_vehicle_brand.get_brand_by_id(vehiclebrand_id, db)
    if not vehiclebrand:
        raise HTTPException(status_code=404, detail="Vehiclebrand not found")
    return vehiclebrand

@router.get("/name/{name}", response_model=VehicleBrand)
def get_vehiclebrands_by_name(name: str, db: Session = Depends(get_db)):
    vehiclebrand = crud_vehicle_brand.get_vehiclebrand_by_name(name, db)
    if not vehiclebrand:
        raise HTTPException(status_code=404, detail="Vehiclebrand not found")
    return vehiclebrand

@router.post("/", response_model=VehicleBrand)
def create_vehiclebrand(vehiclebrand: VehicleBrand, db: Session = Depends(get_db)):
    if not crud_vehicle_brand.get_vehiclebrand_by_name(vehiclebrand.name, db):
        return crud_vehicle_brand.create_vehiclebrand(vehiclebrand, db)
    raise HTTPException(status_code=409, detail="Vehiclebrand Already Exists")

@router.put("/{vehiclebrand_id}",response_model= VehicleBrand)
def update_vehiclebrands(vehiclebrand_id : int , name : str, db:Session = Depends(get_db)):
    return crud_vehicle_brand.update_vehiclebrand(vehiclebrand_id,name,db)


@router.delete("/{vehiclebrand_id}", response_model=VehicleBrand)
def delete_vehiclebrand(vehiclebrand_id: int, db: Session = Depends(get_db)):
    return crud_vehicle_brand.delete_vehiclebrand(vehiclebrand_id, db)
