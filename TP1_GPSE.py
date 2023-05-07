### TP1_AYED-Gritti,Penhalvel,Sosa,Estevez ###

import getpass 
import os
usuario = "admin@shopping.com"
contrasena = "12345"
def clear():   
    os.system('cls')

def construccion_menu():
    print ("En Construccion...")
    menu()
    
def construccion_locales():
    print ("En Construccion...")
    gestion_locales()

def construccion_novedades():
    print ("En Construccion...")
    gestion_novedades()

def menu():
    print("\t MENU")
    print(" (1) Gestion de locales \n (2) Crear cuentas de duenos de locales \n (3) Aprobar/Denegar solicitudes de descuento \n (4) Gestion de novedades \n (5) Reporte de utilizacion de descuentos \n (0) Salir")
    opcion = (input("\nIngrese una opcion: "))
    clear()
    
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
        print ("ERROR. Ingrese una opcion valida")
        print("\t MENU")
        print(" (1) Gestion de locales \n (2) Crear cuentas de duenos de locales \n (3) Aprobar/Denegar solicitudes de descuento \n (4) Gestion de novedades \n (5) Reporte de utilizacion de descuentos \n (0) Salir")
        opcion = (input("\nIngrese una opcion: "))
        clear()
        
    while opcion == "2" or opcion == "3" or opcion == "5":
        construccion_menu()
        opcion = (input("\nIngrese una opcion: "))
        
    if opcion == "1":
        clear()
        gestion_locales()
        
            
    elif opcion == "4":
        clear()
        gestion_novedades()
        
                    
    elif opcion == "0":
        clear()
        print("Gracias por usar el sistema")
        exit()   
        
def check():   
    errores=0
    
    while errores < 3:
        psswd = getpass.getpass(prompt:= "Ingrese la contrasena: ")
        if psswd == contrasena:
            clear()
            menu()
            
        else:
            print("Contrasena incorrecta. Intente nuevamente ")
            errores= errores+1
    else:
        print("Ha ingresado mal la contrasena 3 veces. Finalizando programa.")
        exit()

def login():
    mail = str(input("Ingrese el correo electronico: "))
    while mail != usuario:
        print("Inserte un correo valido")
        mail = str(input("Ingrese el correo electronico: "))
    check()          

def gestion_locales():
    
    
    print("\n \tGESTION DE LOCALES")
    print("\n (a) Crear locales \n (b) Modificar local \n (c) Eliminar local \n (d) Volver ")
    opcion_1 = str(input("\nIngrese una opcion: "))
    clear()
    while opcion_1 != "a" and opcion_1 != "b" and opcion_1 != "c" and opcion_1 != "d":
        print ("ERROR. Ingrese una opcion valida")
        print("\n \tGESTION DE LOCALES")
        print("\n (a) Crear locales \n (b) Modificar local \n (c) Eliminar local \n (d) Volver ")
        opcion_1 = (input("\nIngrese una opcion: "))
        clear()
        
    if opcion_1 == "a":
        clear()
        crear_locales()
                  
    elif opcion_1 == "b" or opcion_1 == "c":
        clear()
        construccion_locales()
        opcion_1 = (input("\nIngrese una opcion: "))
                

    elif opcion_1 == "d":
        clear()
        menu()    

def crear_locales():
    print("\t Crear Locales")

    mayor = 0
    menor = 0 
    perfumeria = 0
    indumentaria = 0
    comida = 0
    nombremayor=""
    nombremenor=""
    
    nombre=input("Ingrese el nombre del local: ")
    while nombre != "volver":
        ubicacion=input("Ingrese la ubicacion del local: ")
        rubro=input("Ingrese el rubro del local: ").lower()
        clear()
        if rubro=="perfumeria":
            perfumeria=perfumeria+1
        elif rubro=="indumentaria":
            indumentaria=indumentaria+1
        elif rubro=="comida":
            comida=comida+1
        else:
            print("Ingrese un rubro valido")
            
        nombre=input("Ingrese el nombre del local: ")
   
    if perfumeria>indumentaria and perfumeria>comida:
        if indumentaria>comida:
            mayor=perfumeria
            menor=comida

    elif indumentaria>comida:
        if comida>perfumeria:
            mayor=indumentaria
            menor=perfumeria
        else:
            mayor=indumentaria
            menor=comida
    elif indumentaria>perfumeria:
        mayor=comida
        menor=perfumeria

    else:
        mayor=comida
        menor=indumentaria

    if mayor==perfumeria:
        nombremayor="perfumeria"
    elif mayor==indumentaria:
        nombremayor="indumentaria"
    else:
        nombremayor="comida"
    
    if menor==perfumeria:
        nombremenor="perfumeria"
    elif menor==indumentaria:
        nombremenor="indumentaria"
    else:
        nombremenor="comida"
             
    print(f"la mayor cantidad de locales es de", nombremayor, "con", mayor, "locales")
    print(f"la menor cantidad de locales es de",nombremenor, "con", menor, "locales")

    gestion_locales()
            
def gestion_novedades():
    print("\n \t GESTION DE NOVEDADES")
    print("\n (a) Crear novedades \n (b) Modificar novedad \n (c) Eliminar novedad \n (d) Ver reporte de novedades \n (e) Volver ")
    opcion_4 = str(input("\nIngrese una opcion: "))
    clear()
    
    while opcion_4 != "a" and opcion_4 != "b" and opcion_4 != "c" and opcion_4 != "d" and opcion_4 != "e":
        print ("ERROR. Ingrese una opcion valida")
        print("\n \t GESTION DE NOVEDADES")
        print("\n (a) Crear novedades \n (b) Modificar novedad \n (c) Eliminar novedad \n (d) Ver reporte de novedades \n (e) Volver ")
        opcion_4 = str(input("\nIngrese una opcion: "))
        clear()
    
        
    if opcion_4 == "a" or opcion_4 == "b" or opcion_4 == "c" or opcion_4 == "d":
        clear()
        construccion_novedades()
            
    elif opcion_4 == "e":
        clear()
        menu()

login() 