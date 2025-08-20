#range generator

'''print(type(range(1,11)))
print(type(range))

def my_range(start,stop):
    i=start
    while i<=stop:
        yield i #e un fel de return,dar returneaza ceva
        i+=1
        if i==4:
            return


gen=my_range(1,10)#valoarea pe care mi o returneaza , este obiectul functiei care urmeaza sa genereze numerele
#nu returneaza valoarea functiei
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration:
    print(next(gen))'''

def is_prime(num):
    count = 0
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count > 2:
            return False
        else:
            return True

def prime_range(start, stop):
    i = start
    while i <= stop:
        if is_prime(i):
            yield i #asta este o forma de a crea un generator
        i += 1
gen = prime_range(2, 100)

print(next(gen))
print(next(gen))
print(next(gen))

try:
    while True:
        print(next(gen))
except StopIteration:
    print("\n Numerele au fost generate")

