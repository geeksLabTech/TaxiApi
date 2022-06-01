from sqlalchemy.orm import Session
import models
from models import table_driver_vehicle
from routers import vehicle_route
from schemas import DriverVehicle


def get_drivervehicle(driver_id: int, vehicle_id: int, db: Session):
    dv = db.query(table_driver_vehicle).all()
    for i in dv:
        if(int(i[0]) == int(driver_id) and int(i[1]) == int(vehicle_id)):
            out = i
            break
    print(out)
    return out


def get_all_drivervehicles(db: Session):
    print(db.query(table_driver_vehicle).all())
    return db.query(table_driver_vehicle).all()


def create_drivervehicle(drivervehicle: DriverVehicle, db: Session):
    driver = db.query(models.DriverDB).filter(models.DriverDB.id == drivervehicle.driver_id).first()
    vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == drivervehicle.vehicle_id).first()
    try:
        driver.vehicles.append(vehicle)
        db.commit()
        return drivervehicle
    except:
        return "Something went Wrong"


def delete_drivervehicle(driver_id: int, vehicle_id: int, db: Session):
    db_drivervehicle = db.query(table_driver_vehicle).filter(
        table_driver_vehicle.driver_id == driver_id, table_driver_vehicle.vehicle_id == vehicle_id).first()
    db.delete(db_drivervehicle)
    db.commit()
    return db_drivervehicle
