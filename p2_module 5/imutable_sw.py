class Switch:
    port = ""
    def add_port(self, port_name):
        self.port=self.port + port_name
        print(self.port)
    # def __init__(self): #prin asta am reparat sa nu mai apara la ambele switch uri create toate porturile si care nu apartin lor
    #     self.ports=[]

sw=Switch()
#print(sw.ports)
sw.add_port("ethernet0")


print("-----")
sw2=Switch()
sw2.add_port("ethernet2")


