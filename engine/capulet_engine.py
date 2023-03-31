from abc import ABC

from car import Car


class CapuletEngine(Car, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
