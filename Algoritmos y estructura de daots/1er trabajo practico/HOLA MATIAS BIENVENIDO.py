import getpass
import os
usuario = "admin@shopping.com"
contrasena = "12345"

def login():
    global mail
    mail = str(input("Ingrese el correo electronico: "))
    while mail != "admin@shopping.com":
        print("Inserte un correo valido")
        mail = str(input("Ingrese el correo electronico: "))
    check()

def clear():   
    os.system('cls')
    
def menu():
    print("\t MENU")
    print(" (1) Gestion de locales \n (2) Crear cuentas de dueños de locales \n (3) Aprobar/Denegar solicitudes de descuento \n (4) Gestion de novedades \n (5) Reporte de utilizacion de descuentos \n (0) Salir")
    global opcion
    opcion = (input("\nIngrese una opcion: "))
    clear()
    
    while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
        print ("ERROR. Ingrese una opcion valida")
        menu()
        
                    
    if opcion == "1":
            clear()
            gestion_locales()
            
    elif opcion == "2":
            clear()
            print("En construccion...")
            menu()
            
            
    elif opcion == "3":
        clear()
        print("En construccion...")  
        menu()
        
    elif opcion == "4":
            clear()
            gestion_novedades()

    elif opcion == "5": 
            clear()
            print("En construccion...")
            menu()          
                
    elif opcion == "0":
        clear()
        print("Gracias por usar el sistema")
        exit()
    
def crear_locales():
    print("\t Crear Locales")
    global indumentaria
    global perfumeria
    global comida
    global mayor
    global menor

    mayor = 0
    menor = 0 
    perfumeria = 0
    indumentaria = 0
    comida = 0
    
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
            print("Ingrese una rubro valido")
            
        nombre=input("Ingrese el nombre del local: ")
        
    

    if perfumeria<indumentaria:
        if perfumeria<comida:
            print(f"La menor cantidad de locales son de comida, con una cantidad de ",perfumeria,"locales")
    elif indumentaria<comida:
            print(f"La menor cantidad de locales son de indumentaria, con una cantidad de ",indumentaria,"locales")
    else:
            print(f"La menor cantidad de locales son de comida, con una cantidad de ",comida,"locales")
            
    if perfumeria>indumentaria:
        if perfumeria>comida:
            print(f"La mayor cantidad de locales son de comida, con una cantidad de ",perfumeria,"locales")
    elif indumentaria>comida:
            print(f"La mayor cantidad de locales son de indumentaria, con una cantidad de ",indumentaria,"locales")
    else:
            print(f"La mayor cantidad de locales son de comida, con una cantidad de ",comida,"locales")
        
    gestion_locales()
        
def gestion_locales():
    
    print("\n \tGESTION DE LOCALES")
    print("\n (a) Crear locales \n (b) Modificar local \n (c) Eliminar local \n (d) Volver ")
    global opcion_1
    opcion_1 = str(input("\nIngrese una opcion: "))
    clear()
    while opcion_1 != "a" and opcion_1 != "b" and opcion_1 != "c" and opcion_1 != "d":
        print ("ERROR. Ingrese una opcion valida")
        gestion_locales()
        
    if opcion_1 == "a":
        clear()
        crear_locales()
                  
    elif opcion_1 == "b" or opcion_1 == "c":
        clear()
        print("En construccion...")
        gestion_locales()
                

    elif opcion_1 == "d":
        clear()
        menu()
          
def gestion_novedades():
    print("\n \t GESTION DE NOVEDADES")
    print("\n (a) Crear novedades \n (b) Modificar novedad \n (c) Eliminar novedad \n (d) Ver reporte de novedades \n (e) Volver ")
    global opcion_4
    opcion_4 = str(input("\nIngrese una opcion: "))
    clear()
    
    while opcion_4 != "a" and opcion_4 != "b" and opcion_4 != "c" and opcion_4 != "d" and opcion_4 != "e":
        print ("ERROR. Ingrese una opcion valida")
        gestion_novedades()
        
    if opcion_4 == "a" or opcion_4 == "b" or opcion_4 == "c" or opcion_4 == "d":
        clear()
        print("En construccion...")
        gestion_novedades()
            
    elif opcion_4 == "e":
        clear()
        menu()

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

login()          
