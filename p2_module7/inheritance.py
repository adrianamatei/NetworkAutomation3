class Vehicle(object):
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def drive(self):
        print("Driving")
class Car(Vehicle):
    def __init__(self, model, year,hand_break=True):
        super().__init__( model, year)
        self.hand_break = hand_break
    def drive(self):
        print(f"Driving car with {self.hand_break}")
class AirPlan(Vehicle):
    def __init__(self, model, year,max_altitude):
        super().__init__(model, year)
        self.max_altitude = max_altitude
    def drive(self):
        print("Flying")
        #print("Drive in Air Plan",Car.drive(self))

a=AirPlan('AirBus',2000,20000)
print(a.model)
print(a.year)
print(a.max_altitude)
a.drive()

delattr(a,'drive')
#delatter(AirPlane,'drive') -> asa se sterge
getattr(a,'drive')
a.drive()
