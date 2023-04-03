import unittest
from random import randint

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarriganTireTesting(unittest.TestCase):
    """
    Testing CarriganTires.needs_service() to return False
    """
    def test_carriganTires_noService_1(self): # testing zero wear on tires
        tire_wear = [0,0,0,0]

        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_serivce())

    def test_carriganTires_noService_2(self): # testing for individual tire on threshold of exceeding wear criteria
        tire_wear = [0,0,0.89,0] # here an assumption is made that the sensor has a resolution of 0.01

        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())
    
    def test_carriganTires_noService_3(self): # testing for multiple tires on threshold value
        tire_wear = [0.89,0,0.89,0.89]

        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_carriganTires_noService_4(self): # testing for random, below threshold wear values on all tires
        tire_wear = [0.23,0.45,0.88,0.34]

        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())

    """
    Testing CarriganTires.needs_service() to return True
    """
    def test_carriganTires_service_1(self): # testing for individual tire on threshold of wear criteria
        tire_wear = [0,0.9,0,0]
        
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())
        
    def test_carriganTires_service_2(self): # testing for multiple tires on threshold of wear criteria
        tire_wear = [0.9,0.9,0.73,0.9]
            
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())
    
    def test_carriganTires_service_3(self): # testing for random over threshold wear values on all tires
        tire_wear = [0.91,0.93,0.94,0.97]
        
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

class OctoprimeTireTesting(unittest.case):
    """
    Testing OctoprimeTires.needs_serivce() to return False
    """
    def test_octoprimeTires_noService_1(self): # testing zero wear on tires
        tire_wear = [0,0,0,0]

        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_octoprimeTires_noService_2(self): # testing for a single tire on the threshold
        tire_wear = [0,0,2.99,0]

        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
    
    def test_octoprimeTires_noService_3(self): # testing for random sum that is on the threshold
        tire_wear = [0.82,0.91,0.83,0.43] # sum of the wear comes to 2.99
        
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
    
    def test_octoPrimeTires_noService_4(self): # testing for random sum that is under the threshold
        tire_wear = [0.81, 0.73, 0,67, 0.54] # sum of the wear comes to 2.75

        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
    
    """
    Testing OctoprimeTires.needs_service() to return True
    """
    def test_octoprimeTires_service_1(self): # testing for threshold wear sum
        tire_wear = [0.83,0.91,0.83,0.43]

        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())
    
    def test_octoprimeTires_service_2(self): # testing for over-threshold sum
        tire_wear = [0.92, 0.93, 0.93, 0.98]

        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

if __name__== '__main__':
    unittest.main()
