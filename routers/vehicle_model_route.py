from fastapi import APIRouter, Depends, HTTPException
from schemas import VehicleModel
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_vehicle_model
from dependencies import get_db


router = APIRouter(
    prefix="/vehiclemodel",
    tags=["VehicleModel"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[VehicleModel])
def get_all_vehiclemodels(db: Session = Depends(get_db)):
    return crud_vehicle_model.get_all_vehiclemodels(db)


@router.get("/{vehiclemodel_id}", response_model=VehicleModel)
def get_vehiclemodels(vehiclemodel_id: int, db: Session = Depends(get_db)):
    vehiclemodel = crud_vehicle_model.get_model_by_id(vehiclemodel_id, db)
    if not vehiclemodel:
        raise HTTPException(status_code=404, detail="VehicleModel not found")
    return vehiclemodel

@router.get("/name/{name}", response_model=VehicleModel)
def get_vehiclemodels_by_name(name: str, db: Session = Depends(get_db)):
    vehiclemodel = crud_vehicle_model.get_vehiclemodel_by_name(name, db)
    if not vehiclemodel:
        raise HTTPException(status_code=404, detail="VehicleModel not found")
    return vehiclemodel

@router.post("/", response_model=VehicleModel)
def create_vehiclemodel(vehiclemodel: VehicleModel, db: Session = Depends(get_db)):
    if not crud_vehicle_model.get_vehiclemodel_by_name(vehiclemodel.name, db):
        return crud_vehicle_model.create_vehiclemodel(vehiclemodel, db)
    raise HTTPException(status_code=409, detail="VehicleModel Already Exists")

@router.put("/{vehiclemodel_id}",response_model= VehicleModel)
def update_vehiclemodels(vehiclemodel_id : int , name : str, brand_id: int, seats: int, db:Session = Depends(get_db)):
    return crud_vehicle_model.update_vehiclemodel(vehiclemodel_id,name, brand_id, seats,db)


@router.delete("/{vehiclemodel_id}", response_model=VehicleModel)
def delete_vehiclemodel(vehiclemodel_id: int, db: Session = Depends(get_db)):
    return crud_vehicle_model.delete_vehiclemodel(vehiclemodel_id, db)