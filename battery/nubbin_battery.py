from datetime import datetime
from battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
         service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
         return True if service_threshold_date < datetime.today().date() else False