var="string"
print(type(var))
#print(int(var))-aceasta conversie nu se poate face
#print(int('10_000'))
#putem scrie numerele si cu _


var2=2
print(type(var2))
print(type(str(var2)))

#lista poate contine elemente de tipuri diferite
var3=['string',2]
print(type(var3))
print(str(var3))

var4=10.3
print(type(var4))


var5=1+ 2j
print(type(var5))
#key le pot fi orice obiecte , string, int
var6={'':2}
print(type(var6))

#nu pot converti un set intr un int 
#din set se elimina duplicatele, ordinea in interiorul unui set nu este definita, le afiseaza intr o ordine random
var7={'abc','abc','abcd'}
print(type(var7))
print(var7)


