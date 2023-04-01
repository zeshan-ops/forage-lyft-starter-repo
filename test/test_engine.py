import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CapuletEngineTesting(unittest.TestCase):
    """
    Testing CapuletEngine.needs_service() to return False
    """
    def test_capuletEngine_noService_1(self): # testing both mileage values same number
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(CapuletEngine.needs_service())

    def test_capuletEngine_noService_2(self): # testing mileage values different
        current_mileage = 11
        last_service_mileage = 10

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(CapuletEngine.needs_service())

    def test_capuletEngine_noService_3(self): # testing mileage values on threshold
        current_mileage = 51235
        last_service_mileage = 21235

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(CapuletEngine.needs_service())

    """
    Testing CapuletEngine.needs_service() to return True
    """
    def test_capuletEngine_noService_2(self): # testing mileage values over threshold
        current_mileage = 112546
        last_service_mileage = 31920

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(CapuletEngine.needs_service())

    def test_capuletEngine_noService_3(self): # testing mileage values on threshold
        current_mileage = 102392
        last_service_mileage = 82391

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(CapuletEngine.needs_service())   

if __name__ == '__main__':
    unittest.main()