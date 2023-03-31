from car import Car
from datetime import datetime
from car_factory import CarFactory

def test_battery():
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 3)
    last_service_mileage = 20000
    current_mileage = 50000

    testCalliope = CarFactory.create_calliope(last_service_date, current_mileage, last_service_mileage)
    print(testCalliope.needs_service())

test_battery()