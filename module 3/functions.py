#avem doua tipuri de argumente
def function1(arg1,arg2,keyarg1=None,keyarg2=None):
    print(arg1,arg2,keyarg1,keyarg2)


function1('message1','message2')
function1('message1','message2', keyarg1='message3', keyarg2='message4')

try:
    function1('message1')
except TypeError:
    print("required positional argument")

#order of arguments
#def function1(keyarg1=None,arg1,arg2,keyarg2=None):
 #   print(arg1,arg2,keyarg1,keyarg2)

 #argument packing -
def function2(*args,argn):
    print(args,argn)

function2('message1','message2','message3', argn='messagen')

# *var pack unpack variables
a=10
b=20
a,b=b,a #switch vars
print(a,b)

a,b,c=[1,2,3]
print(a,b,c)

a,*b,c=[1,2,3,4,5]
print(a,b,c)
#a,*b,*c=[1,2,3,4,5] -> aici nu merge , primul obiect fura totul, adica b
#print(a,b,c)

#argument packing
def function4(karg_n=None,**kargs):
    print(karg_n,kargs)
function4(arg1=1,arg2=2, karg_n='new_value')

dict(key='value')
print(dict(key='value'))
print(dict(((1,2),(3,4),)))

#**args =((1,2),(3,4)) ?

#global, local si nonlocat vars , astea 3 tipuri de variabile , local tot ce e definit in interiroul unui bloc de cod al uei functii, nonlocal cele care trebuie accesate de alte functii din interiorul functiei in care este definit

var_g=10
print('value of g ', var_g)
def function5(arg1,arg2,keyarg1=None,keyarg2=None):
    global var_g
    var_g=15
    print('global variable from outside function',var_g) #global variable

    print(arg1,arg2,keyarg1,keyarg2)#all local variables
print('value of g',var_g)
#print(arg)
function5('message1','message2')
print('value of g',var_g)
print('----------------------------------')
var_non_l=5
def function6():
    var_non_l=10
    def function7():
        nonlocal var_non_l
        var_non_l=20
        print(var_non_l)
    function7()
    print('var_non_l',var_non_l)
    return function7
f2=function6()

print("-----------------------------")
var_non_l=5
def function6():
    var_non_l=10
    def function7():
        nonlocal var_non_l
        var_non_l=20
        print(var_non_l)
        def function8():
            nonlocal var_non_l
            var_non_l = 20
            print(var_non_l)

    function7()
    print('var_non_l',var_non_l)
    return function7
f2=function6()





print('-------------')
#functie care returneaza primele 100 de numere primi

def is_prime(num):
    count = 0
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1
        if count > 2:
            return False
        else:
            return True

prime = []
n = 2
while len(prime) < 100:
    if is_prime(n):
        prime.append(n)
    n =n+1

print(prime)


print("-----varianta Robert din timpul sedintei----")
def prime():
    prime_counter=0
    nrs=3
    print("1","2")
    while prime_counter <=100:
        for i in range(2, nrs//2+1):
            if not nrs % i :
                break
        else:
             prime_counter = prime_counter + 1
             print(nrs)
        nrs=nrs+1

    return


result=prime()
print(result)
print("---------------------------------")

#keyword ul return
#function as object



def generic_function(message):
    print('generic function',message)

def add_function(message:str ):
    pass

def multiple_functions(message:str ):
    pass

list_of_functions=[generic_function,add_function, multiple_functions]
print([generic_function])
user_message=input("enter message: ")
user_function=input("enter your function")
generic_function(user_message)

for f in list_of_functions:
    if user_function in f.__name__:
        found_function=f
        print('found function', found_function.__name__)

print(found_function(user_message))

