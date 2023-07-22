import getpass as get
import os

""" Array precargado con 'codigo', 'usuario', 'clave', 'tipo' """
users_db = [["1", "4", "6", "9"],
            ["admin@shopping.com", "localA@shopping.com", "localB@shopping.com", "unCliente@shopping.com"],
            ["12345", "AAAA1111", "BBBB2222", "33xx33"],
            ["administrador", "dueñoLocal", "dueñoLocal", "cliente"]] 


def login(db):
    """ Inicio de sesion como administrador """
    count = 0
    flag = False
    position = False

    while count <= 3:
        os.system("cls")
        
        if flag == False:
            user_validation = str(input("Ingresa el mail del usuario: "))
            for i in range(4):
                if db[1][i] == user_validation:
                    position = i
                    flag = True

        if not position:
            count += 1
            print("el usuario no existe \n Presiona enter para volver a intentarlo")
            input()

            if count == 3:
                return (False,)
        else:
            password_validation = get.getpass("Ingresa la contraseña: ")
            if db[2][position] == password_validation:
                return (db[0][position], db[1][position], db[2][position], db[3][position], True,)
            else:
                count += 1
                print("La contraseña es incorrecta \n Presione enter para volver a intentarlo")
                input()

                if count == 3:
                    return (False,)


def menu_admin():
    print(""" 
        1. Gestión de locales
        2. Crear cuentas de dueños de locales
        3. Aprobar / Denegar solicitud de descuento
        4. Gestión de Novedades
        5. Reporte de utilización de descuentos
        0. Salir""")


def sub_menu_gestion():
        print(f'''
        a) Crear locales
        b) Modificar local
        c) Eliminar local
        d) Mapa de locales"
        e) Volver''')


def menu_novedad():
    print("""Gestión de novedades
a) Crear novedades
b) Modificar novedad
c) Eliminar novedad
d) Ver reporte de novedades
e) Volver
""")


def menu_clientela():
    print("""
1. Registrarme
2. Buscar descuentos en locales
3. Solicitar descuento
4. Ver novedades
0. Salir
""")


def menu_dueño():
    print("""1. Gestión de Descuentos
a) Crear descuento para mi local
b) Modificar descuento de mi local
c) Eliminar descuento de mi local
d) Volver
2. Aceptar / Rechazar pedido de descuento
3. Reporte de uso de descuentos
0. Salir""")
    

def search_shops(obj, db):
    flag = False
    start = 0
    end = 50
    while not start > end or flag:
        middle = (start + end) // 2
        if db[middle] == obj:
            flag = True
        elif db[middle] > obj:
            end = middle - 1
        else: 
            start = middle + 1
    if flag:
        return True
    else:
        return False


def create_shops(db, shops):
    flag = False
    code = int(input("Ingrese tu código de usuario: "))

    if code == db[0]:

        name = str("Por favor ingresa el nombre del local: ")
        while flag != True:
            if search_shops(name, shops):
                flag = True
            else:
                name = str("Por favor ingresa el nombre del local: ")
                
        ubication = input("Ingrese la ubicación del local: ")
        area = str(input("Ingrese el rubro: "))

        while area != "indumentaria" or area != "perfumería" or area != "comida":
            print("No existe el rubro, ingrese otro")
            area = str(input("Ingrese el rubro: "))
        
        


        
        

def show_menu(current_user):
    
    if current_user[3] == "administrador":
        menu_admin()

        option = int(input("Ingresa la accion que desea realizar: "))

        while option != 0:
            os.system("cls")

            if option == 1:
                os.system("cls")
                sub_menu_gestion()

                option = str(input("Ingresa la accion que desea realizar: "))

                if option == "a":
                    create_shops(current_user, shops)

                elif option == "b" or option == "c":
                    print("En construcción …\n Presiona enter para continuar")
                    input()

                elif option == "d":
                    print("")
            
            if option == 2 or option == 3 or option == 5:
                print("En construcción …\n Presiona enter para continuar")
                input()

            if option == 4:
                os.system("cls")
                sub_menu_novedades()

                option = str(input("Ingresa la accion que desea realizar: "))

                if option == "a" or option== "b" or option =="c" or option== "d":
                    print("En construcción …\n Presiona enter para continuar")
                    input()

                elif option == "e":
                    print("")
            os.system("cls")
            menu_admin()
            option = int(input("Ingresa la accion que desea realizar: "))
        

id = 0
shops = [[None for x in range(50)] for x in range(3)]

validation = login()

if validation[-1]:
    show_menu(validation, shops)