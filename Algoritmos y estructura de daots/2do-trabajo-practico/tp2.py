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
    position = 9999

    while count <= 3:
        os.system("cls")
        
        if flag == False:
            user_validation = str(input("Ingresa el mail del usuario: "))
            for i in range(4):
                if db[1][i] == user_validation:
                    position = i
                    flag = True

        if position == 9999:
            count += 1
            print("el usuario no existe \n Presiona enter para volver a intentarlo")
            input()

            if count == 3:
                return (False,)
        else:
            password_validation = get.getpass("Ingresa la contraseña: ")
            if db[2][position] == password_validation:
                return (db[0][position],
                        db[1][position],
                        db[2][position],
                        db[3][position],
                        True,)
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
    
# Funcionalidades de locales
"""def search_shops(obj, db: list, line: str):
    flag = False
    start = 0
    end = 50
    while not (start > end or flag):
        middle = (start + end) // 2
        if db[line][middle] == obj:
            flag = True
        elif db[line][middle] > obj:
            end = middle - 1
        else: 
            start = middle + 1
    if flag:
        return True, middle
    else:
        return False """

def search(db, col, longi, obj):
    q=False
    comi = 0
    fin = longi - 1
    for k in range(0,longi):
        while not (comi > fin or q):
            medio = (comi + fin)//2
            if obj == db[medio][col]:
                q = True
            elif obj < db[medio][col]:
                fin = medio-1
            else:
                comi = medio+1

    if q:
        return 1
    else:
        return 0
            

def search_obj(arreglo, nombre_objetivo):
    if not arreglo:
        return False

    filas = len(arreglo)
    izquierda = 0
    derecha = filas - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        nombre_medio = arreglo[medio][1]

        if nombre_medio == nombre_objetivo:
            return True
        elif nombre_medio < nombre_objetivo:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return False


def order(db,column,limit):
 for i in range(0,limit-1):
    for k in range(i+1,limit):
      if db[i][column] < db[k][column]:
        for w in range(colums):
            aux=db[i][w]
            db[i][w]=db[k][w]
            db[k][w]=aux


def modify_shops(code: int, db: list):
    flag = False
    obj = search(db, code, 0)
    if obj[0]:
        option = str(input("Desea modificar el nombre? Si/No"))
        option.lower()
        if option == "si":
            new_name = str(input("Ingresa el nuevo nombre: "))
            while flag != True:
                if search(obj=new_name, db=db, line=1):
                    flag = True
                    save_in_db(id=db[0][obj[1]], db=db, name=new_name, ubication=db[2][obj[1]], area=db[3][obj[1]])
                else:
                    print("El nombre ya esta en uso")
                    new_name = str(input("Ingresa el nuevo nombre: "))

        option = str(input("Desea modificar el ubicacion? Si/No"))
        option.lower()
        if option == "si":
            new_ubication = str(input("Ingresa la nueva ubicacion: "))
            save_in_db(id=db[0][obj[1]], db=db, name=db[1][obj[1]], ubication=new_ubication, area=db[3][obj[1]])

        option = str(input("Desea modificar el rubro? Si/No"))
        option.lower()
        if option == "si":
            new_area = str(input("Ingresa el nuevo rubro: "))
            save_in_db(id=db[0][obj[1]], db=db, name=db[1][obj[1]], ubication=db[2][obj[1]], area=new_area)
        print("Guardado con exito! 【 ͡❛ ͜ʖ ͡❛】👍")
        input()
    else:
        print("No existe local con ese codigo")
        input()


def save_in_db(db, line, id, name, ubication, area, is_active):
    global i
    db[i][0] = id
    db[i][1] = name
    db[i][2] = ubication
    db[i][3] = area
    db[i][4] = is_active
 
    i+=1
    order(db,1,line)
    if i > 50:
        return "No se ha podido guardar su local porque no hay más lugares disponibles"
    else:
        return "Local guardado"



def create_shops(current_user: tuple, db: list):
    global id
    flag = False
    code = str(input("Ingrese tu código de usuario: "))

    if code == current_user[0]:

        name = str(input("Por favor ingresa el nombre del local: "))
        while flag != True:
            #_search = search(db, 1, fil, name)
            _search = search_obj(db, name)
            if _search is not True:
                flag = True
            else:
                print("El nombre ya existe, elija otro")
                name = str(input("Por favor ingresa el nombre del local: "))
                
        ubication = input("Ingrese la ubicación del local: ")
        area = str(input("Ingrese el rubro: "))

        while not (area != "indumentaria" or area != "perfumería" or area != "comida"):
            print("No existe el rubro, ingrese otro")
            area = str(input("Ingrese el rubro: "))
        
        id += 1
        response = save_in_db(db=db, line=fil, id=id, name=name, ubication=ubication, area=area, is_active=True)
        print(db)
        input()
        print(response)


def show_menu(current_user: tuple):
    
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

                elif option == "b":
                    code = int(input("ingrese el codigo del local que desea modificar: "))
                    modify_shops(code=code, db=shops)

                elif option == "d":
                    print("")
            
            if option == 2 or option == 3 or option == 5:
                print("En construcción …\n Presiona enter para continuar")
                input()

            if option == 4:
                os.system("cls")
                pass

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
i = 0
fil=6
colums=6
shops= [""] * fil
for f in range(fil):
    shops[f]=[""] * colums

validation = login(users_db)

if validation[-1]:
    show_menu(validation)
