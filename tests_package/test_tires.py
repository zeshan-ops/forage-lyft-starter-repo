import unittest
from random import randint

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarriganTireTesting(unittest.TestCase):
    """
    Testing CarriganTires.needs_service() to return False
    """
    def test_CarriganTires_noService_1(self): # testing zero wear on tires
        tire_wear = [0,0,0,0]

        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_serivce())

    def test_CarriganTires_noService_2(self): # testing for individual tire on threshold of exceeding wear criteria
        for i in range(0,3):
            tire_wear = [0,0,0,0]
            tire_wear[i] = 0.89 # here we have made the assumption that the tyre wear sensors can give accuracy to 0.01

            tires = CarriganTires(tire_wear)
            self.assertFalse(tires.needs_service())
    
    def test_CarriganTires_noService_3(self): # testing for multiple tires on threshold value
        for i in range(0,3):
            tire_wear = [0,0,0,0]
            for j in range(0,i):
                tire_wear[j] = 0.89
            
            tires = CarriganTires(tire_wear)
            self.assertFalse(tires.need_service())

    def test_CarriganTires_noService_4(self): # testing for random, below threshold wear values on all tires
        tire_wear = [0,0,0,0]
        for i in range(0,3):
            tire_wear[i] = randint(0,89)/100
        
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.need_service())
        
if __name__ == '__main__':
    unittest.main()
