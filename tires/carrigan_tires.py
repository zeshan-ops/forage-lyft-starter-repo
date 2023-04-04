from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
    
    def needs_service(self):
        wear_exceeded = False
        for i in range(0,4):
            if(self.tire_wear[i] > 0.89):
                wear_exceeded = True
        return wear_exceeded