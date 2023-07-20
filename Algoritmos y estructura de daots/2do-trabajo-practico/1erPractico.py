import getpass as get
import os


def login():
    """ Inicio de sesion como administrador """
    global user, password

    count = 0

    while count <= 3:
        os.system("clear")

        user_validation = str(input("Ingresa el mail del usuario: "))
        password_validation = get.getpass("Ingresa la contraña: ")

        if user == user_validation:
            if password == password_validation:
                return True
            else:
                count += 1
                print(
                    "La contraseña es incorrecta\n Presiona enter para volve a intentarlo")
                input()

                if count == 3:
                    return False

        else:
            count += 1
            print("El usuario es incorrecto\nPresiona enter para volve a intentarlo")
            input()

            if count == 3:
                return False


def menu():
        print('''
        1. Gestión de locales
        2. Crear cuentas de dueños de locales
        3. Aprobar / Denegarsolicitud de descuento
        4. Gestión de novedades
        5. Reporte de utilización de descuentos
        0. Salir
        ''')


def sub_menu_gestion():
        print('''
        a) Crear locales
        b) Modificar local
        c) Eliminar local
        d) Mapa de locales    
        e) Volver
        ''')


def sub_menu_novedades():
        print('''
        a) Crear novedades
        b) Modificar novedad
        c) Eliminar novedad
        d) Ver reporte de novedades
        e) Volver
        ''')


def crear_locales():
        shops = 5
        cant_indumentaria = 0
        cant_perfumeria = 0
        cant_comida = 0
        rubro_local = 'asd'

        for i in range(shops):
            os.system("clear")
            print("Ingresa el tipo de rubro que quieres para tu local\n---\nTipos de rubros: \n -indumentaria  \n -perfumería  \n -comida\n\nEn caso de no querer ingresar mas locales, tipear 'salir'\n")
            rubro_local = str(input("Indique la opcion que desea: "))
            rubro_local.lower()
                
            if rubro_local == "salir":
                return ""

            nombreLocal = str(input("Ingresa el nombre del local: "))
            ubi_local = str(input("Ingresa la ubicacion del local: "))

            if rubro_local == "indumentaria" or rubro_local == "perfumeria" or rubro_local == "comida":
                shops -= 1
                print(f"El nombre del local es {nombreLocal}, que está ubicado en {ubi_local}. Está dentro del rubro de {rubro_local}\n-Presiona enter para continuar")
                input()

                if rubro_local == "indumentaria":
                    cant_indumentaria += 1

                if rubro_local == "perfumeria":
                    cant_perfumeria += 1

                if rubro_local == "comida":
                    cant_comida += 1

            while rubro_local != "indumentaria" and rubro_local != "perfumeria" and rubro_local != "comida":
                print("Por favor indique un rubro dentro de las opciones")
                input()
                rubro_local = str(input("Indique el rubro del local: "))


        if cant_comida == 0 and cant_perfumeria == 0 and cant_indumentaria == 0:
            print("No has creado ningun local")
            input()
            return True

        elif cant_comida == cant_perfumeria == cant_indumentaria:
            print(f"Los tres rubros tienen la misma cantidad de locales con un total de {cant_comida}")
            input()
            return True
        
        elif cant_comida == cant_indumentaria and cant_comida > cant_perfumeria:
            print(f"los rubros que tienen una mayor cantidad de locales son indumentaria y comida con un total de {cant_comida} cada uno.")  
            print(f"el rubro con menos locales es Perfumeria con un total de {cant_perfumeria}")
            input()
            return True

        elif cant_comida == cant_perfumeria and cant_comida > cant_indumentaria:
            print(f"los rubros que tienen una mayor cantidad de locales son perfumeria y comida con un total de {cant_comida} cada uno.")  
            print(f"el rubro con menos locales es Indumentaria con un total de {cant_indumentaria}")
            input()
            return True
        
        elif cant_indumentaria == cant_perfumeria and cant_perfumeria > cant_comida :
            print(f"los rubros que tienen una mayor cantidad de locales son perfumeria e indumentaria con un total de {cant_indumentaria} cada uno.")
            print(f"el rubro con menos locales es Comida con un total de {cant_comida}")
            input()
            return True
        
        if cant_comida == cant_indumentaria and cant_comida < cant_perfumeria:
            print(f"los rubros que tienen una mayor cantidad de locales son indumentaria y comida con un total de {cant_comida} cada uno.")  
            print(f"el rubro con menos locales es Perfunmeria con un total de {cant_perfumeria}")
            input()
            return True

        elif cant_comida == cant_perfumeria and cant_comida < cant_indumentaria:
            print(f"los rubros que tienen una mayor cantidad de locales son perfumeria y comida con un total de {cant_comida} cada uno.")  
            print(f"el rubro con menos locales es Indumentaria con un total {cant_indumentaria}")
            input()
            return True
        
        elif cant_indumentaria == cant_perfumeria and cant_comida < cant_comida :
            print(f"los rubros que tienen una mayor cantidad de locales son perfumeria e indumentaria con un total de {cant_indumentaria} cada uno.")
            print(f"el rubro con menos locales es Comida con un total de {cant_comida}")
            input()
            return True
        
        elif cant_comida > cant_indumentaria and cant_comida > cant_perfumeria:
            print(f"El rubro con mas locales es Comida con un total de {cant_comida} locales")
            if cant_indumentaria > cant_perfumeria:
                print(f"El rubro con menos locales es Perfumería con un total de {cant_perfumeria} locales")
                input()
                return True
                
            else:
                print(f"El rubro con menos locales es Indumentaria con: {cant_indumentaria} ")
                input()
                return True
        elif cant_indumentaria > cant_perfumeria:
            print(f"El rubro con mas locales es Indumentaria con un total de {cant_indumentaria} locales")
            print(f"El rubro con menos locales es Comida con un total de {cant_comida} locales")
            input()

        else:
            print(f"El rubro con mas locales es Perfumeria con un total de {cant_perfumeria} locales")
            if cant_indumentaria > cant_comida:
                print(f"El rubro con menos locales es Comida con un total de {cant_comida} locales")
                input()
                return True
            else:
                print(f"El rubro con menos locales es Indumentaria con un total de {cant_indumentaria} locales")
                input()
                return True


def show_menu():
    menu()
    option = int(input("Ingresa la accion que desea realizar: "))

    while option != 0:
        os.system("clear")

        if option == 1:
            os.system("clear")
            sub_menu_gestion()

            option = str(input("Ingresa la accion que desea realizar: "))

            if option == "a":
                crear_locales()

            elif option == "b" or option == "c":
                print("En construcción …\n Presiona enter para continuar")
                input()

            elif option == "d":
                print("")
        
        if option == 2 or option == 3 or option == 5:
            print("En construcción …\n Presiona enter para continuar")
            input()

        if option == 4:
            os.system("clear")
            sub_menu_novedades()

            option = str(input("Ingresa la accion que desea realizar: "))

            if option == "a" or option== "b" or option =="c" or option== "d":
                print("En construcción …\n Presiona enter para continuar")
                input()

            elif option == "e":
                print("")
        os.system("clear")
        menu()
        option = int(input("Ingresa la accion que desea realizar: "))
        

user = "admin@shopping.com"
password = "12345"

validation = login()

if validation == True:
    show_menu()