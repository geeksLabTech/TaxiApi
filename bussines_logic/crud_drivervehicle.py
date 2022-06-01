from sqlalchemy.orm import Session
import models
from models import table_driver_vehicle
from routers import vehicle_route
from schemas import DriverVehicle


def get_drivervehicle(driver_id: int, vehicle_id: int, db: Session):
    return db.query(table_driver_vehicle).filter(table_driver_vehicle.driver_id == driver_id, table_driver_vehicle.vehicle_id == vehicle_id).first()


def get_all_drivervehicles(db: Session):
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


# def update_drivervehicle(db: Session, driver_id: int, vehicle_id: int, drivervehicle: DriverVehicle):
#     db_drivervehicle = db.query(table_driver_vehicle).filter(
#         table_driver_vehicle.driver_id == driver_id, table_driver_vehicle.vehicle_id == vehicle_id).first()
#     db_drivervehicle.driver_id = drivervehicle.driver_id
#     db_drivervehicle.vehicle_id = drivervehicle.vehicle_id


def delete_drivervehicle(driver_id: int, vehicle_id: int, db: Session):
    db_drivervehicle = db.query(table_driver_vehicle).filter(
        table_driver_vehicle.driver_id == driver_id, table_driver_vehicle.vehicle_id == vehicle_id).first()
    db.delete(db_drivervehicle)
    db.commit()
    return db_drivervehicle
