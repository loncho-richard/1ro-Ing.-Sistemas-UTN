sumadorP = 0
problemas_resuetos = 0

opcion = str(input("Quieres resolver un problema: "))


while opcion == "si":
    if opcion == "si":
        pA = str(input("A Piensas que puees resolcer el problema? "))
        pB = str(input("B Piensas que puees resolcer el problema? "))
        pC = str(input("C Piensas que puees resolcer el problema? "))
        if pA == "si" and pB == "si":
            print("El problema esta resuelto")
            sumadorP += 1

        if pB == "si" and pC == "si":
            print("El problema esta resuelto")
            sumadorP += 1

        if pA == "si" and pC == "si":
            print("El problema esta resuelto")
            sumadorP += 1

        else:
            print("El problema no esta resuelto")
            
    else:
        print("Ingresa un opcion correcta")
    
    problemas_resuetos += 1

    opcion = str(input("Quieres resolver un problema: "))

print(f"El porcentaje de problemas resueltos es: {sumadorP/problemas_resuetos*100}")