'''class Triangle:
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c

#vreau input de la utilizator care sa dicteze ce latura sa modifc
t=Triangle(1,1,1)
change=(input('Provide len for new side ex: (a: 2) ' )).strip('( )').strip(':')
key,value=list(map(lambda _: int(_.strip()) if _.strip().isdigit() else _.strip(),change.split(':')))

print(key,value)

#t.a=2 #set attribute

setattr(t,key,value)
print(getattr(t,key))'''
#LUCRU CU TRIUNGHI ADEVARAT
class Triangle:
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c
    #ne definim propria metoda
    def __setattr__(self, key, value):
        #x=getattr(self,key)
        super().__setattr__(key,value+1)
       # print(dir(self))
        #print(key)
    def __delattr__(self, key):
        super().__delattr__(key)
    def __getattr__(self, key):
        return super().__getattribute__(key)




#vreau input de la utilizator care sa dicteze ce latura sa modifc
t=Triangle(1,1,1)
change=(input('Provide len for new side ex: (a: 2) ' )).strip('( )').strip(':')
key,value=list(map(lambda _: int(_.strip()) if _.strip().isdigit() else _.strip(),change.split(':')))

print(key,value)

#t.a=2 #set attribute
#t.__setattr__('example','value')


setattr(t,key,value)
#t.__setattr__(key,value)
print(getattr(t,key))

#print(t.__getattribute__(key))


print(t.a)
delattr(t,key)
#t.__delattr__(key)
print(getattr(t,key))
print(t.a)