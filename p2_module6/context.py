#context am mai folosit la fisiere
import time


class CrashCar(Exception):
    print("Car crashed")
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print("Constructing")
        #evitam prin asta
        time.sleep(0.1)
    def drive(self):
        print('Driving...')
        time.sleep(0.1)
        #raise CrashCar
        raise AttributeError("Mesaj")

    def __enter__(self):
        print('Entering...')
        time.sleep(0.1)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit...')
        if exc_type is CrashCar:
            print('Calling Ambulance')
        #print(exc_type, exc_val, exc_tb)
            return True
        return False
with Car(2001,'Dacia') as car:
    car.drive()

#avem nevoie de context
