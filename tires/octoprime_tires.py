from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        tire_wear_sum = 0
        for i in range(0,4):
            tire_wear_sum += self.tire_wear[i]
        return True if tire_wear_sum > 2.99 else False