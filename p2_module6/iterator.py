#un iterator, in cazul unui loop for luam un obiect iterabil
class CarIterator():
    def __init__(self, model,year,whiles):
        self.model=model
        self.year=year
        self.whiles=whiles
    def __iter__(self):
        return self
    def __next__(self):
       # raise StopIteration
       if self.whiles:
            value=self.whiles
            self.whiles-=1
       else:
           raise StopIteration
       return value


class Car():
    def __init__(self, model:str,year:int,whiles:int):
        self.model = model
        self.year = year
        self.whiles = whiles
    def __iter__(self):
        return CarIterator(model=self.model,year=self.year,whiles=self.whiles)

car=Car('Mercedes',2019,4)
for c in car:
    print(c)

#steps for the loop
car_iter=car.__iter__()
print(next(car_iter))
print(next(car_iter))
print(next(car_iter))
print(next(car_iter))
print(next(car_iter))

'''class BookIterator:
    def __init__(self, pages):
        self.pages = pages
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.pages):
            value = self.pages[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __iter__(self):
        return BookIterator(self.pages)


book = Book("About flowers", ["Page 1", "Page 2", "Page 3"])
for page in book:
    print(page)

book_iter = book.__iter__()
print(next(book_iter))
print(next(book_iter))
print(next(book_iter))
print(next(book_iter))
print(next(book_iter))
'''

'''
class OralCavityIterator:
    def __init__(self, teeth, cavities):
        self.teeth = teeth
        self.cavities = cavities

    def __iter__(self):
        return self

    def __next__(self):
        if self.teeth and (self.teeth not in self.cavities):
            value = self.teeth
            self.teeth -= 1
        elif self.teeth in self.cavities:
            value = 99
            self.teeth -= 1
        else :
            raise StopIteration
        return value

class OralCavity:
    def __init__(self, teeth, cavities):
        self.teeth = teeth
        self.cavities = cavities

    def __iter__(self):
        return OralCavityIterator(teeth=self.teeth, cavities=self.cavities)


or_cav = OralCavity(32, [1,5,7])

for o in or_cav:
    print(o)
 
'''