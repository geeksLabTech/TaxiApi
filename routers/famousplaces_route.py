from fastapi import APIRouter, Depends, HTTPException
from schemas import FamousPlaces
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_famousplaces
from dependencies import get_db


router = APIRouter(
    prefix="/famousplaces",
    tags=["FamousPlaces"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[FamousPlaces])
def get_all_famousplaces(db: Session = Depends(get_db)):
    return crud_famousplaces.get_all_famousplaces(db)


@router.get("/{famousplaces_id}", response_model=FamousPlaces)
def get_famousplaces(famousplaces_id: int, db: Session = Depends(get_db)):
    famousplace = crud_famousplaces.get_famousplace(famousplaces_id, db)
    if not famousplace:
        raise HTTPException(status_code=404, detail="FamousPlaces not found")
    return famousplace

@router.get("/name/{name}", response_model=FamousPlaces)
def get_famousplaces_by_name(name: str, db: Session = Depends(get_db)):
    famousplace = crud_famousplaces.get_famousplaces_by_name(name, db)
    if not famousplace:
        raise HTTPException(status_code=404, detail="FamousPlaces not found")
    return famousplace

router.post("/", response_model=FamousPlaces)
def create_famousplace(famousplaces: FamousPlaces, db: Session = Depends(get_db)):
    return crud_famousplaces.create_famousplace(famousplaces, db)

router.delete("/{famousplaces_id}", response_model=FamousPlaces)
def delete_famousplace(famousplaces_id: int, db: Session = Depends(get_db)):
    return crud_famousplaces.delete_famousplace(famousplaces_id, db)