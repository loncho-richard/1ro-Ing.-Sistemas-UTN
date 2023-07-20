import getpass as get
import os


users_db = [["1", "4", "6", "9"],
            ["admin@shopping.com", "localA@shopping.com", "localB@shopping.com", "unCliente@shopping.com"],
            ["12345", "AAAA1111", "BBBB2222", "33xx33"],
            ["administrador", "dueñoLocal", "dueñoLocal", "cliente"]] 


def login(db):
    """ Inicio de sesion como administrador """
    count = 0
    aux = False
    position = False

    while count <= 3:
        os.system("cls")
        
        if aux == False:
            user_validation = str(input("Ingresa el mail del usuario: "))
            for i in range(4):
                if db[1][i] == user_validation:
                    position = i
                    aux = True

        if not position:
            count += 1
            print("el usuario no existe \n Presiona enter para volver a intentarlo")
            input()

            if count == 3:
                return False
        else:
            password_validation = get.getpass("Ingresa la contraseña: ")
            if db[2][position] == password_validation:
                return True, db[3][position]
            else:
                count += 1
                print("La contraseña es incorrecta \n Presione enter para volver a intentarlo")
                input()

                if count == 3:
                    return False

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

