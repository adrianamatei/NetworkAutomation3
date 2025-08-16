import telnetlib3
import sys
from module4.example_import import example_var, example_func1
from example_package import package_variable, example_func2
#varianta mai scurta nerecomandata
# from example_package import *
# from module4.example_import import *
print(example_var)
print(package_variable)
example_func1()
example_func2()
#print(i)



from module4.example_import import example_var, example_func1
import example_package as ep #in cazul acesta acest modul devine o variabila si ce e in interiroul lui va fi accesibil prin .

print(ep)
print(ep.example_func2())

print(sys.path)


