from abc import ABC
from datetime import datetime
from battery import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
         return True if service_threshold_date < datetime.today().date() else False