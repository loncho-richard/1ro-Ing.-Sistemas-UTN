import getpass as get
import os


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
    print('''
        1. Gestión de locales
        2. Crear cuentas de dueños de locales
        3. Aprobar / Denegar solicitud de descuento
        4. Gestión de Novedades
        5. Reporte de utilización de descuentos
        0. Salir''')


def sub_menu_gestion():
        print('''
        a) Crear locales
        b) Modificar local
        c) Eliminar local
        d) Mapa de locales
        e) Volver''')


def menu_novedad():
    print('''
        Gestión de novedades
        a) Crear novedades
        b) Modificar novedad
        c) Eliminar novedad
        d) Ver reporte de novedades
        e) Volver''')


def menu_clientela():
    print('''
        1. Registrarme
        2. Buscar descuentos en locales
        3. Solicitar descuento
        4. Ver novedades
        0. Salir''')


def menu_dueño():
    print('''
        1. Gestión de Descuentos
        2. Aceptar / Rechazar pedido de descuento
        3. Reporte de uso de descuentos
        0. Salir''')
    

def sub_menu_dueño():
    print('''
        a) Crear descuento para mi local
        b) Modificar descuento de mi local
        c) Eliminar descuento de mi local
        d) Volver''')
    
# Funcionalidades de locales
 

def search_obj(db, obj, column):
    if not db:
        return False

    rows = len(db)
    left = 0
    right = rows - 1

    while left <= right:
        middle = (left + right) // 2

        obj_middle = db[middle][column]

        if obj_middle == obj:
            return True, middle
        elif obj_middle < obj:
            right = middle - 1
        else:
            left = middle + 1

    return False,


def busqueda_por_corrimiento(arreglo, id_objetivo):
    for idx, fila in enumerate(arreglo):
        if fila[0] == id_objetivo:
            return idx

    return None


def order(db,column,limit):
 for i in range(0,limit-1):
    for k in range(i+1,limit):
      if db[i][column] < db[k][column]:
        for w in range(colums):
            aux=db[i][w]
            db[i][w]=db[k][w]
            db[k][w]=aux


def modify_shops(code: str, db: list):
    flag = False
    obj = search_obj(db, code, 1)
    idx = db[0][obj[1]]
    row = busqueda_por_corrimiento(db, idx)
    status = db[obj[1]][5]
    if status == True:
        if obj[0] and row is not None:
            option = str(input("Desea modificar el nombre? Si/No: "))
            option.lower()
            if option == "si":
                new_name = str(input("Ingresa el nuevo nombre: "))
                while flag != True:
                    _search = search_obj(obj=new_name, db=db, column=1)
                    if not _search[0]:
                        flag = True
                        save_in_db(i=row, id=db[obj[1]][0], db=db, line=fil, name=new_name, ubication=db[obj[1]][2], area=db[obj[1]][3], user_code=db[obj[1]][4], is_active=db[obj[1]][5])
                    else:
                        print("El nombre ya esta en uso")
                        new_name = str(input("Ingresa el nuevo nombre: "))

            option = str(input("Desea modificar el ubicacion? Si/No"))
            option.lower()
            if option == "si":
                new_ubication = str(input("Ingresa la nueva ubicacion: "))
                save_in_db(i=row, id=db[obj[1]][0], db=db, line=fil, name=db[obj[1]][1], ubication=new_ubication, area=db[obj[1]][3], user_code=db[obj[1]][4], is_active=db[obj[1]][5])

            option = str(input("Desea modificar el rubro? Si/No: "))
            option.lower()
            if option == "si":
                new_area = str(input("Ingresa el nuevo rubro: "))
                save_in_db(i=row, id=db[obj[1]][0], db=db, line=fil, name=db[obj[1]][1], ubication=db[obj[1]][2], area=new_area, user_code=db[obj[1]][4], is_active=db[obj[1]][5])

            print("Guardado con exito! 【 ͡❛ ͜ʖ ͡❛】👍")
            input()
        else:
            print("No existe local con ese codigo")
            input()
    else:
        print("El local no esta activo o no existe")


def delete_shops(db, name_shop, code_shop):
    question = str(input("Estas seguro que deseas elimir el local!? Si/No: "))
    question.lower()
    if question == "si":
        obj = search_obj(db, name_shop, 1)
        idx = db[0][obj[1]]
        row = busqueda_por_corrimiento(db, idx)
        
        if code_shop == idx:
            db[row][5] = False

        else:
            print("El id del local no corresponde al local ingresado")
            input()


def save_in_db(i, db, line, id, name, ubication, area, user_code,is_active):
    db[i][0] = id
    db[i][1] = name
    db[i][2] = ubication
    db[i][3] = area
    db[i][4] = user_code
    db[i][5] = is_active
 
    order(db,1,line)
    if i > 50:
        return "No se ha podido guardar su local porque no hay más lugares disponibles"
    else:
        return "Local Guardado con exito! 【 ͡❛ ͜ʖ ͡❛】👍"



def create_shops(current_user: tuple, db: list):
    global id, i
    flag = False
    code = str(input("Ingrese tu código de usuario: "))

    if code == current_user[0]:

        name = str(input("Por favor ingresa el nombre del local: "))
        while flag != True:
            _search = search_obj(db, name, 1)
            if _search[0] is not True:
                flag = True
            else:
                print("El nombre ya existe, elija otro")
                name = str(input("Por favor ingresa el nombre del local: "))
                
        ubication = input("Ingrese la ubicación del local: ")
        area = str(input("Ingrese el rubro: "))

        while not(area == "indumentaria" or area == "perfumería" or area == "comida"):
            print("No existe el rubro, ingrese otro")
            area = str(input("Ingrese el rubro: "))

        user_code = input("Ingresa el codigo de usuario del dueño de este local: ")
        while user_code == users_db[3][1] or user_code == users_db[3][2]:
            print("Este codigo no pertenece a algun dueño de local existente, pruebe de nuevo...")
            user_code = input("Ingresa el codigo de usuario del dueño de este local: ")        
        
        id += 1
        i += 1
        response = save_in_db(i, db=db, line=fil, id=id, name=name, ubication=ubication, area=area, user_code=user_code,is_active=True)
        print(response)
        print(f"Id del local: {id} \nNombre: {name} \nUbicaciones: {ubication} \nRubro: {area} \nCodigo del dueño: {user_code} \nEstatus: {True}")
        input()


def question(idx):
    if idx is int:
        if idx < 10:
            return f"|O{idx}"
    elif idx == "":
        return "|00"
    else:
        return f"|{idx}"

def map_shops(db):
    i = 0
    for floor in range(1):
        print(f"Piso {floor + 1}")
        for row in range(10):
            print("+--+--+--+--+--+")
            id_1 = db[i][0]
            i += 1
            id_2 = db[i][0]
            i += 1
            id_3 = db[i][0]
            i += 1
            id_4 = db[i][0]
            i += 1
            id_5 = db[i][0]
            i += 1  
            print(f"{question(id_1)}{question(id_2)}{question(id_3)}{question(id_4)}{question(id_5)}|")
        
        print("+--+--+--+--+--+")
        print("     (...)      ")


def show_shops(db):
    print("Locales...")
    for i in range(len(shops)):
        print("____________________")
        print(f"Id del local: {db[i][0]} \nNombre: {db[i][1]} \nUbicaciones: {db[i][2]} \nRubro: {db[i][3]} \nCodigo del dueño: {db[i][4]} \nEstatus: {db[i][5]}")


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
                while option != "e":
                    if option == "a":
                        sub_option = str(input("Desea ver los locales hasta el momento antes de ingresar uno nuevo? Si/No"))
                        sub_option.lower()
                        if sub_option == "si":
                            show_shops(shops)
                            input()
                            os.system("cls")


                        create_shops(current_user, shops)

                    elif option == "b":
                        sub_option = str(input("Desea ver los locales hasta el momento antes de ingresar uno nuevo? Si/No"))
                        sub_option.lower()
                        if sub_option == "si":
                            show_shops(shops)
                            input()
                            os.system("cls")

                        code = str(input("Ingrese el nombre del local que desea modificar: "))
                        modify_shops(code=code, db=shops)

                    elif option == "c":
                        sub_option = str(input("Desea ver los locales hasta el momento antes de ingresar uno nuevo? Si/No"))
                        sub_option.lower()
                        if sub_option == "si":
                            show_shops(shops)
                            input()
                            os.system("cls")

                        name_shop = str(input("Ingresa el nombre del local que desea elimir: "))
                        code_shop = int(input("Ingresa el codigo del local que se desea eliminar: "))
                        delete_shops(db=shops, name_shop=name_shop, code_shop=code_shop)
                    
                    elif option == "d":
                        os.system("cls")
                        map_shops(shops)
                        print("Presiona enter para continuar")
                        input()
                        
                    os.system("cls")
                    sub_menu_gestion()
                    option = str(input("Ingresa la accion que desea realizar: "))
            
            if option == 2 or option == 3 or option == 5:
                print("En construcción …\n Presiona enter para continuar")
                input()

            if option == 4:
                os.system("cls")
                menu_novedad()

                option = int(input("Ingresa la accion que desea realizar: "))

                if option == "a" or option== "b" or option =="c" or option== "d":
                    print("En construcción …\n Presiona enter para continuar")
                    input()

                elif option == "e":
                    print("")
            os.system("cls")
            menu_admin()
            option = int(input("Ingresa la accion que desea realizar: "))

    elif current_user[3] == "dueñoLocal":
        
        menu_dueño()
        option = int(input("Ingresa la accion que desea realizar: "))

        while option != 0:

            if option == 1:
                sub_menu_dueño()
                
                option = str(input("Ingresa la accion que desea realizar: "))

                while option != "d":
                    
                    if option == "a" or option == "b" or option == "c":
                        print("En construcción …\n Presiona enter para continuar")
                        input()
                    
                    sub_menu_dueño()
                    option = str(input("Ingresa la accion que desea realizar: "))

            elif option == 2 or option == 3:
                print("En construcción …\n Presiona enter para continuar")
                input()

            menu_dueño()
            option = int(input("Ingresa la accion que desea realizar: "))

    elif current_user[3] == "cliente":

        menu_clientela()
        option = int(input("Ingresa la accion que desea realizar: "))

        while option != 0:
            if option == 1 or option == 2 or option == 3 or option == 4:
                print("En construcción …\n Presiona enter para continuar")
                input()

            menu_clientela()
            option = int(input("Ingresa la accion que desea realizar: "))


""" Array precargado con 'codigo', 'usuario', 'clave', 'tipo' """
users_db = [["1", "4", "6", "9"],
            ["admin@shopping.com", "localA@shopping.com", "localB@shopping.com", "unCliente@shopping.com"],
            ["12345", "AAAA1111", "BBBB2222", "33xx33"],
            ["administrador", "dueñoLocal", "dueñoLocal", "cliente"]] 


id = 0
i = 0
fil=50
colums=6
shops= [""] * fil
for f in range(fil):
    shops[f]=[""] * colums

validation = login(users_db)

if validation[-1]:
    show_menu(validation)
