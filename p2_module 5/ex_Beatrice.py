class Switch:
    ports = [] #porturil sunt practic o lista , daca elimin asta va da eroare comanda Switch.ports
    def add_port(self, port_name):
        self.ports.append(port_name)
        print(self.ports)
    def __init__(self): #prin asta am reparat sa nu mai apara la ambele switch uri create toate porturile si care nu apartin lor
        self.ports=[]

#ambele switch uri au referinta la acceasi locatie de memorie, aceeasi lista
sw=Switch()
#print(sw.ports)
sw.add_port("ethernet0")
#print(sw.ports)

print("-----")
sw2=Switch()
sw2.add_port("ethernet2")
#print(sw2.ports)

#metode de reparare, in init cream practic o lista goala de porturi pentru fiecare switch al nostru

print(Switch.ports)