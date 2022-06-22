from fastapi import APIRouter, Depends, HTTPException
from schemas import Place
from typing import List
from sqlalchemy.orm import Session
from bussines_logic import crud_place
from dependencies import get_db


router = APIRouter(
    prefix="/place",
    tags=["Place"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Place])
def get_all_places(db: Session = Depends(get_db)):
    return crud_place.get_all_places(db)


@router.get("/{place_id}", response_model=Place)
def get_place(place_id: int, db: Session = Depends(get_db)):
    place = crud_place.get_place(place_id, db)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place


@router.get("/name/{name}", response_model=Place)
def get_place_by_name(name: str, db: Session = Depends(get_db)):
    place = crud_place.get_place_by_name(name, db)
    if not place:
        raise HTTPException(status_code=404, detail="Place not found")
    return place


@router.post("/", response_model=Place)
def create_place(place: Place, db: Session = Depends(get_db)):
    return crud_place.create_place(place, db)

@router.put("/{place_id}",response_model= Place)
def update_places(place_id : int , name : str , address :str , latitude : str , longitude :str , db:Session = Depends(get_db)):
    return crud_place.update_place(place_id,name,address,latitude,longitude,db)


@router.delete("/{place_id}", response_model=Place)
def delete_place(place_id: int, db: Session = Depends(get_db)):
    return crud_place.delete_place(place_id, db)

