
from fastapi import FastAPI
from routers import driver_route, drivervehicle_route, famousplaces_route, passenger_route, place_route, trip_route, vehicle_route
#from database import SessionLocal, engine
import models
#from .tests.test_sql_app import client

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(passenger_route.router)
app.include_router(driver_route.router)
app.include_router(place_route.router)
app.include_router(famousplaces_route.router)
app.include_router(trip_route.router)
app.include_router(vehicle_route.router)
app.include_router(drivervehicle_route.router)



    
