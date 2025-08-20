#create list of functions where function is x+ Y and Y is incremented from 1 to 100
'''list_of_func = []
for number in range(1, 101):
   # func = lambda x,y=number: x + y-> solutia Alexandra(1p)
    func=lambda x:x+number
    list_of_func.append(func)

print(list_of_func)
print(list_of_func[0](2))
print(list_of_func[1](2))
'''



'''def save_value(y):
    return lambda x: x + y

list_of_func = []
for number in range(1, 101):
    list_of_func.append(save_value(number))'''

list_of_func = [lambda x, y=n: x + y for n in range(1, 101)]

print(list_of_func[0](2) )  # 3  -> 2 + 1
print(list_of_func[1](2) )  # 4  -> 2 + 2

