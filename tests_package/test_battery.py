import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class NubbinBatteryTesting(unittest.TestCase):
    """
    Testing NubbinBattery.needs_service() to return False
    """
    def test_NubbinBattery_noService_1(self): # testing both service dates the same value
        last_service_date = datetime.today().now()
        current_date = last_service_date

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
    
    def test_NubbinBattery_noService_2(self): # testing threshold service dates
        last_service_date = datetime.today().now()
        current_date = last_service_date.replace(year=last_service_date.year + 4)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_NubbinBatter_noService_3(self): # testing non-threshold service dates
        current_date = datetime.today().now()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    """
    Testing NubbinBattery.needs_service() to return True
    """
    def test_NubbinBattery_service_1(self): # testing threshold service dates
        current_date = datetime.today().now()
        last_service_date = current_date.replace(year=current_date.year - 4)
        last_service_date = last_service_date.replace(microsecond=last_service_date.microsecond - 1)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())
    
    def test_NubbinBattery_service_2(self): # testing non-threshold service dates
        current_date = datetime.today().now()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())   

class SpindlerBatteryTesting(unittest.TestCase):
    """
    Testing SpindlerBattery.needs_service() to return False
    """
    def test_SpindlerBattery_noService_1(self): # testing both service dates the same value
        last_service_date = datetime.today().now()
        current_date = last_service_date

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
    
    def test_SpindlerBattery_noService_2(self): # testing threshold service dates
        last_service_date = datetime.today().now()
        current_date = last_service_date.replace(year=last_service_date.year + 3)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_SpindlerBatter_noService_3(self): # testing non-threshold service dates
        current_date = datetime.today().now()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    """
    Testing SpindlerBattery.needs_service() to return True
    """
    def test_SpindlerBattery_service_1(self): # testing threshold service dates
        current_date = datetime.today().now()
        last_service_date = current_date.replace(year=current_date.year - 3)
        last_service_date = last_service_date.replace(microsecond=last_service_date.microsecond - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_SpindlerBattery_service_2(self): # testing non-threshold service dates
        current_date = datetime.today().now()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()