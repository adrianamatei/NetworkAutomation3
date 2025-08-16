import random


class Car(object):
    class_var="generic_car"
    color="red"
#self este biectul creat cu clasa asta in 90% din cazuri
    def __init__(self,speed):
        print('car id is: ', id(self))
        #self.color = color
        self.speed = speed
    def drive(some_object):
        print("id in drive of object",id(some_object))
        print('driving car at speed: ', some_object.speed)
    @staticmethod #primul tip de metoda, nu mai depinde de instanta
    def print_something():
        print(f"Something random: {random.randint(0,100)}")
    #al doilea tip de metoda care depinde de clasa, nu de instanta
    def paint_car(self, color):
        print("painting car ",color)
        self.color = color
    #@staticmethod
    @classmethod
    def get_default_car_color(cls):
        return Car.color
    def __str__(self):#pentru cand vreau sa afisez ca string
        return f'{self.__class__.__name__} with speed {self.speed} and color {self.color}'

    def __repr__(self): #pentru reprezentare cand face parte din lista
        return f'{self.__class__.__name__}--{self.speed}--{self.color}'


car= Car(200)
car.print_something()
print(car.color)
car.paint_car('blue')
print('Default color is:',car.get_default_car_color())
print(car.__class__)
print(car)
# var1="test"
# print("test")
#pot controla si pt masina sa se afiseze frumos
var1=str(car)
print(var1)

car1=Car(201)
car2=Car(202)
car3=Car(203)
garage=[car1,car2,car3]
print(garage)
