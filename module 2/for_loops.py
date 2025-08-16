for var1 in range(10):
    print(var1)
print("------")
for var1 in [1,'1',None]:
    print(var1)

print("--------")
# ++ to
var1=[1,'1',None]
var2=var1.__iter__()
print(var2.__next__())
print(var2.__next__())
print(var2.__next__())
#print(var2.__next__()) stopIteration causes the loop to end
print("----------")
#keyword for 'for' loop
for var1 in [1,2,3]:
    if var1==1:
        continue#va intrerupe executia si se intoarce la reevaluare
    print(var1)
print(80*"*")
for var1 in [1,2,3]:
    if var1==1:
        break
    print(var1)

#keyword else pentru for
print("----------")


for continue_ in [None]:
    if continue_:
        break
        #continue
    print(continue_)
else:#se executa doar cand for ul ajunge la ultima iteratie
    print("loop finished ")

print("value is:",continue_)#value from last iteration, value may be undefined



