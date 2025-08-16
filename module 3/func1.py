from math import prod
'''print("----------------------------")
def generic_function(message):
    print('generic function',message)

def add_function(message:str ):
    sum_=0
    try:
        l=message.split(',')
        for item in l:
            sum_=sum_+float(item)
    except:
        print("Something went wrong")
    return sum_

def multiple_functions(message:str ):
    p = 1
    try:
        numbers = message.split(',')
        for item in numbers:
            p=p*float(item)
        return p
    except:
        print("Something went wrong")

list_of_functions=[generic_function,add_function, multiple_functions]
print([generic_function])
user_message=input("enter message: ")
user_function=input("enter your function: ")
generic_function(user_message)

match user_function:
    case '+' | 'add':
        user_function = 'add_function'
    case '*' | 'multiple':
        user_function = 'multiple_functions'
    case 'generic':
        user_function = 'generic_function'
    case _:
        print("Function not found")
        user_function = None
found_function=None

for f in list_of_functions:
    if user_function and user_function in f.__name__:
        found_function = f
        print('found function', found_function.__name__)
        break

if found_function:
    print(found_function(user_message))
else:
    print("No matching function executed.")

#facem un match , ca user ul sa poata face cu operatia de "+", nu cu add


print("----varianta cu maparea intr un dictionar------")

def generic_function(message):
    print('generic function',message)

def add_function(message:str ):
    sum_=0
    try:
        l=message.split(',')
        for item in l:
            sum_=sum_+float(item)
    except:
        print("Something went wrong")
    return sum_

def multiple_functions(message:str ):
    operands = str(message).split(',')
    operands_v2:list[int]=[]
    for index,number in enumerate(operands):
        operands[index] = int(number)

    p = 1
    try:
        numbers = message.split(',')
        for item in numbers:
            p=p*float(item)
        return p
    except:
        print("Something went wrong")
        '''

'''



list_of_functions=[generic_function,add_function, multiple_functions]
dict_of_functions={'*':multiple_functions,'+':add_function,'_':generic_function}
print([generic_function])
user_message=input("enter message: ")
user_function=input("enter your function: ")
generic_function(user_message)

for f in list_of_functions:
    if user_function and user_function in f.__name__:
        found_function = f
        print('found function', found_function.__name__)
try:
    found_function
except NameError:
    for key, f  in dict_of_functions.items():
        if key==user_function:
            found_function = f
print(found_function(user_message))

'''