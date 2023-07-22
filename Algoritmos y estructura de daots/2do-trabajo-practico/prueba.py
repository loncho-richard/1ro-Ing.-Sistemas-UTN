""" shops = [[None for x in range(5)] for x in range(3)]
 """
shops = ['jorge', 'munta', 'coto']


name = str(input("Ingrese el nombre del local: "))
i = 0
maximo = 50
while i <= maximo:
    if name == shops[i]:
        i = 0
        print("Este nombre ya esta registrado")
        name = str(input("Ingrese un nombre del local válido: "))
    else: 
        i += 1