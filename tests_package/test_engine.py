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
        self.assertFalse(engine.needs_service())

    def test_capuletEngine_noService_2(self): # testing mileage values different
        current_mileage = 11
        last_service_mileage = 10

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_capuletEngine_noService_3(self): # testing mileage values on threshold
        current_mileage = 51235
        last_service_mileage = 21235

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    """
    Testing CapuletEngine.needs_service() to return True
    """
    def test_capuletEngine_service_1(self): # testing mileage values over threshold
        current_mileage = 112546
        last_service_mileage = 31920

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capuletEngine_service_2(self): # testing mileage values on threshold
        current_mileage = 112392
        last_service_mileage = 82391

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())   

class WillougbhyEngineTesting(unittest.TestCase):
    """
    Testing WilloughbyEngine.needs_service() to return False
    """
    def test_willoughbyEngine_noService_1(self): # testing both mileage values same number
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughbyEngine_noService_2(self): # testing mileage values different
        current_mileage = 11
        last_service_mileage = 10

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_willoughbyEngine_noService_3(self): # testing mileage values on threshold
        current_mileage = 81235
        last_service_mileage = 21235

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    """
    Testing WilloughbyEngine.needs_service() to return True
    """
    def test_willoughbyEngine_service_1(self): # testing mileage values over threshold
        current_mileage = 112546
        last_service_mileage = 31920

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughbyEngine_service_2(self): # testing mileage values on threshold
        current_mileage = 120001
        last_service_mileage = 60000

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

class SternmanEngineTesting(unittest.TestCase):
    """
    Testing SternmanEngine.needs_service() to return False 
    """
    def test_sternmanEngine_noService(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())
    
    """
    Testing SternmanEngine.needs_service() to return True
    """
    def test_sternmanEngine_service(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()