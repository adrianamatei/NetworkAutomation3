#clasele le utilizam ca sa creem obiectele necesare
#la nivelul clasei se comporta si actioneaza la fel ca si o functie
dict(key=1) #calls constructor of class dict

#definirea unei clase, punem numele cu litera mare
class SomeObject(object):
    pass
# def some_function():
#     print("some function")

class Car(object):
    class_var="generic_car"
#self este biectul creat cu clasa asta in 90% din cazuri
    def __init__(self, color, speed):
        print('car id is: ', id(self))
        self.color = color
        self.speed = speed
    def drive(some_object):
        print("id in drive of object",id(some_object))
        print('driving car at speed: ', some_object.speed)



car=Car('blue',200)
print(id(car))
print(car.color)
print(car.speed)
print(car.class_var)
print(Car.class_var)
print(Car.drive)
print(car.drive)
#object_with_speed='test'
#object_with_speed.speed=200 #cannot be changed for built ins
#Car.drive(object_with_speed)
so=SomeObject()
so.speed=50
Car.drive(so)

#so.x=some_function()
#so.x()
print("Some object id: " , id(so))
print("Car id" ,id(car))

print(car.drive)
car.drive() # echivalent cu Car.drive(car)



# print(id(Car.class_var))
# print(id(car.class_var))#acelasi id
#inseamna practic ca se share uie locatia de memorie intre instantele clasei


