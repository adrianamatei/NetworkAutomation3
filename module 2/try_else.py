#try nu accepta niciun argument, folosit pentru cod care ar putea genera exceptii
#print(1/0) python nu stie sa lucreze cu infinit
try:
    print("running")
    raise KeyboardInterrupt
    #while True:
     #   print("do something")
    #print(1 / 0)
    #x + y
    assert False


#trebuie o ordine clara de definire a exceptiilor



except (ZeroDivisionError,AssertionError) as e:
#puteam pune mia multe erorii,puneam cu ,
    print("something went wrong",f"'{e}'")

#asta mai mult pentru cazurile in care nu stiu ce exceptie s a intamplat
except Exception as e: #exception prinde aproape orice exceptie
    print(e)
    #raise
#except BaseException as e: #asta e o exceptie si mai generala
 #   print("for all other cases")#in general nu se foloseste base exception si nici except:
  #  raise e #ca sa vad intreaga exceptie, de la prima linie de unde o aparut
else: #se executa doar cand nu avem nicio expceptie, altfel nu se executa
    print("all is good")
finally:#se executa in orice caz
    print("This will always be print")