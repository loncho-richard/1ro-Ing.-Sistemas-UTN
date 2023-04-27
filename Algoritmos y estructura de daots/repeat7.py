num_bus = 0
max_pas = 0
pasajeros = 0
peso_total = 0
equipaje = 0

def ingreso():
    global pasajeros
    global equipaje
    global peso_total
    peso_total += equipaje
    pasajeros += 1
    equipaje = int(input("Cual es el peso del equipaje? "))
    
num_bus = int(input("Ingrese numero del micro:"))
max_pas = int(input("Maximo de pasajeros:"))              

equipaje = int(input("Cual es el peso del equipaje? "))
while (peso_total+equipaje <= 3500 and pasajeros < max_pas) or equipaje == 0:
    peso_total += equipaje
    pasajeros += 1
    equipaje = int(input("Cual es el peso del equipaje? "))

print("Numero del micro: ", int(num_bus) , "\n Numero de pasajeros: " , int(pasajeros))
if pasajeros == max_pas:
    print("El micro va lleno")