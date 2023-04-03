from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory(Car):
    def create_calliope(current_date,last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date))
    
    def create_glissade(current_date,last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),
            SpindlerBattery(last_service_date,current_date))
    
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(last_service_date,current_date))
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),
            NubbinBattery(last_service_date, current_date))
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(CapuletEngine(current_mileage,last_service_mileage),
            NubbinBattery(last_service_date, current_date))