from sqlalchemy.orm import Session
import models
from models import table_driver_vehicle
from routers import vehicle_route
from schemas import DriverVehicle


def get_drivervehicle(driver_id: int, vehicle_id: int, db: Session):
    driver = db.query(models.DriverDB).filter(models.DriverDB.id == driver_id).first()
    vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == vehicle_id).first()
    
    if vehicle in driver.vehicles:
        return {
            "driver_id": driver_id,
            "vehicle_id": vehicle_id
            }


def get_all_drivervehicles(db: Session):
    print(db.query(table_driver_vehicle).all())
    return db.query(table_driver_vehicle).all()


def create_drivervehicle(drivervehicle: DriverVehicle, db: Session):
    driver = db.query(models.DriverDB).filter(models.DriverDB.id == drivervehicle.driver_id).first()
    vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == drivervehicle.vehicle_id).first()
    
    driver.vehicles.append(vehicle)
    db.commit()
    return drivervehicle
    

def delete_drivervehicle(driver_id: int, vehicle_id: int, db: Session):
    driver = db.query(models.DriverDB).filter(models.DriverDB.id == driver_id).first()
    vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == vehicle_id).first()
    try:
        driver.vehicles.remove(vehicle)
        db.commit()
        return {'message': 'DriverVehicle deleted'}
    except:
        return "Something went Wrong"
