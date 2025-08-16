import time

try:
    f = open('file.txt')
    file=open("test.txt","w")
    file.write("hello world")
    raise Exception
    file.flush()
    file.close()
    file=open("test.txt","r")
    print(file.read())
    file.close()

#o sa folosim mereu urm sintaxa , nu pe prima
    with open("test.txt","r") as file:
        response=file.read()
    print(response)
except:
      time.sleep(15)

try:
    with open("test.txt","w") as file:
        file.write("hello world")
        raise Exception
    print(response)
except:
    time.sleep(15)