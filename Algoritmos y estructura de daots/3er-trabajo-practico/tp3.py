import os
import pickle
import datetime
import getpass as get

#Arreglo global
Locales = [[]*6]*50

# Declaracion de clases
class User():
    def __init__(self):
        self.codeUs = 0
        self.email = ""
        self.password = ""
        self.user_type = ""

class Local():
    def __init__(self):
        self.codeLocal = 0
        self.name = ""
        self.ubi = ""
        self.rubro = ""
        self.codeUs = 0
        self.status= ""

class Promo():
    def __init__(self):
        self.codPromo = 0
        self.textPromo = ""
        self.fechaIniP = 0 
        self.fechaFinP = 0
        self.dSemana = []*6     # int
        self.estatus = ""
        self.codeLocal = 0

class Use_Promo():
    def __init__(self):
        self.codClient = 0
        self.codPromo = 0
        self.fechaUP = 0

class News():
    def __init__(self):
        self.codNews = 0
        self.textNews = ""
        self.fechaIniN = 0 
        self.fechaFinN = 0
        self.user_type = ""

# Textos
def menu():
    print("""
    1-Ingresar con usuario registrado
    2-Registrarse como cliente
    0-salir""")
    
def menu_cliente():
    print("""
    1-Buscar descuentos en local
    2-Solicitar descuento
    0-Salir
        """)

def menu_admin():
    print("""
    1. Gestión de locales
    2. Crear cuentas de dueños de locales
    3. Aprobar / Denegar solicitud de descuento
    4. Gestión de Novedades
    5. Reporte de utilización de descuentos
    0. Salir
    """)

def sub_menu_admin():
    print("""
    a)Creal locales.
    b)Modificar locales.
    c)Eliminar locales.
    d)Mapa de locales.
    e)Volver.
    """)

def menu_owner():
    print("""
    1. Crear descuento
    2. Reporte de uso de descuentos
    0. Salir
    """)

def dicotomica(afisico, alogico, valor):
    alogico.seek(0)
    t = os.path.getsize(afisico)
    aux = pickle.load(alogico)
    UnReg = alogico.tell
    fin = t // UnReg
    ini = 1
    q = False
    while not q and ini <= fin:
        med = (ini+fin) // 2
        alogico.seek(med * UnReg)
        Reg = pickle.load(alogico)
        if Reg.dato == valor:
            q = True
        elif Reg.dato < valor:
            ini = med + 1
        else:
            fin = med -1
    if q:
        return True
    else:
        return False

def ordenar_archivo(afisico, alogico): #LLEVAR LOS REGISTROS A UN ARREGLO Y DESPUÉS VOLCARLO DEVUELTA EN EL ARCHIVO.
    global Locales
    t = os.path.getsize(afisico)
    alogico.seek(0)
    aux = pickle.load(alogico)
    PesoUnReg = alogico.tell()
    long = t// PesoUnReg
    for i in range(long):
        Locales[i][0] = aux.codeLocal
        Locales[i][1] = aux.name   
        Locales[i][2] = aux.ubi
        Locales[i][3] = aux.rubro  
        Locales[i][4] = aux.codeUs
        Locales[i][5] = aux.status
        aux = pickle.load(alogico)
    
"""class Local():
    def __init__(self):
        self.codeLocal = 0
        self.name = ""
        self.ubi = ""
        self.rubro = ""
        self.codeUs = 0
        self.status= """ 


# Login, usuando los modelos de User
def login(afUser, alUser):
    count = 0
    flag1 = False
    flag2 = False
    position = 9999

    while count <= 3:
        os.system("cls")
        
        if flag1 == False:
            user_validation = str(input("Ingresa el email del usuario: "))
            while flag2 == False:
                alUser.seek(0)
                user = pickle.load(alUser)
                user_password = user.password
                if user.email == user_validation:
                    position = alUser.tell()
                    flag1 = True
                    flag2 = True

        if position == 9999:
            count += 1
            print("el usuario no existe \n Presiona enter para volver a intentarlo")
            input()

            if count == 3:
                return (False,)
        else:
            password_validation = get.getpass("Ingresa la contraseña: ")
            
            if user_password == password_validation:
                return (True, user,)
            else:
                count += 1
                print("La contraseña es incorrecta \n Presione enter para volver a intentarlo")
                input()

                if count == 3:
                    return (False,)

# Funcion por barrido para encontrar si existe o no le usuario
def busquedaxbarrido(afisico, alogico, email):
        flag1 = False
        tam = os.path.getsize(afisico)
        alogico.seek(0)
        while alogico.tell() < tam or flag1:
            aux = pickle.load(alogico)
            if aux.email == email:
                flag1= True
        if flag1 == True:
            return False
        else:
            return True
def busquedaxbarrido_CodeDueno(afisico, alogico, cod):
        flag1 = False
        tam = os.path.getsize(afisico)
        alogico.seek(0)
        while alogico.tell() < tam or flag1:
            aux = pickle.load(alogico)
            if aux.codeUs == cod:
                if aux.user_type == "Dueño de Local":
                    flag1= True
        if flag1:
            return True
        else:
            return False
def busquedaxbarrido_ModificarLocales(afisico, alogico, current_user):
        flag1 = False
        tam = os.path.getsize(afisico)
        alogico.seek(0)
        while alogico.tell() < tam or flag1:
            aux = pickle.load(alogico)
            if aux.codeLocal == current_user.codeUS:
                flag1= True
        if flag1 == True:
            return False
        else:
            return True
def busquedaxbarrido_NombreLocal(afisico, alogico, nom):
        flag1 = False
        tam = os.path.getsize(afisico)
        alogico.seek(0)
        while alogico.tell() < tam or flag1:
            aux = pickle.load(alogico)
            if aux.name == nom:
                flag1= True
        if flag1 == True:
            return True
        else:
            return False    
# Funcion para crear Usuarios, dependiendo del "user_type", podemos crear un "cliente" o un "dueño local"
def signup(afUser, alUser, user_type):
    os.system("cls")
    """
        self.codeUs = 0
        self.email = ""
        self.password = ""
        self.user_type =
    """ 
    flag2 = False
    existe = True
    email = obtener_input_con_limite("Email: ", 100)
    existe = busquedaxbarrido(afUser, alUser, email)
    while existe == False:
        print("Esta mail ya está ingresado, ingrese otro")
        email = obtener_input_con_limite("Email: ", 100)
        existe = busquedaxbarrido(afUser, alUser,email)


    while flag2 == False:
        password = obtener_input_con_limite("Contraseña: ", 8)
        re_password = obtener_input_con_limite("Repetir contraseña: ", 8)
        if password == re_password:
            flag2 = True
        else:
            print("Las contraseñas no coinciden, presiona enter para volver a intentarlo...")
            input()
    uid = busqueda_del_ultimo(alUser, afUser)
    uid += 1
    client = User()
    client.codeUs = uid
    client.email = email
    client.password = password
    client.user_type = user_type
    print(client)
    pickle.dump(client, alUser)

# Funcion para buscar el ultimo id, y poder crear un id autoincrementable
def busqueda_del_ultimo(alogico, afisico):
    t = os.path.getsize(afisico)
    alogico.seek(0)
    unreg = pickle.load(alogico)
    tamaño_un_reg = alogico.tell()
    cant_reg = t // tamaño_un_reg
    byte_ultimo_reg = (cant_reg - 1) * tamaño_un_reg
    alogico.seek(byte_ultimo_reg)
    ultimo_reg = pickle.load(alogico)
    ultimoId = ultimo_reg.codeUs
    return ultimoId

# Input con limit, "maxlength"
def obtener_input_con_limite(prompt, limite):
    while True:
        entrada = input(prompt)
        if len(entrada) <= limite:
            return entrada
        else:
            print(f"La entrada debe tener como máximo {limite} caracteres.")

def menu_administrador():
    menu_administrador()
    op = int(input("ingrese que opción quiere realizar: "))
    validar_op(op,0,5)
    match op:
        case 1:
            gestion_de_locales()
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 0:
            pass


def crear_locales():
    global aflocales,allocales,alUser,afUser
    desicion = input("¿Desea crear un local?(Si/No)")
    desicion.lower()
    while desicion != "si" and desicion != "no":
        desicion = input("Ingrese opcion valida(Si/No)")
    while desicion = "si":   
        nomb = input("Ingrese el nombre de su nuevo local: ")
        existenom = busquedaxbarrido_NombreLocal(aflocales, allocales, nomb)
        flag4 = True
        intentosnom = 0
        while existenom and flag4:
            nomb = input("Nombre ya existente, ingrese otro: ")
            existenom = busquedaxbarrido_NombreLocal(aflocales, allocales, nomb)
            intentosnom += 1
            if intentosnom = 3:
                flag4 = False
        ubi = input("Ingrese la ubicacion del local (por ejemplo ‘primer piso, ala este, sector B): ")
        cod = int(input("Ingrese su codigo de dueño de local:"))
        existecod = busquedaxbarrido_CodeDueno(afUser,alUser,cod)
        flag3 = True
        intentos = 0
        while not existecod and flag3:
            cod = int(input("Su codigo de dueño de local no existe o no es de tipo dueño, ingrese otro:"))
            existecod = busquedaxbarrido_CodeDueno(afUser,alUser,cod)
            intentos += 1
            if intentos == 3:
                flag3 = False
        rubro = input("""Ingrese el rubro de su local (Disponibles : Perfumería, Indumentaria o Comida): """)
        rubro.lower()
        while rubro != "perfumeria" and rubro != "indumentaria" and rubro != "comida":
            rubro = input("""Su rubro no existe, ingrese otro (Perfumería, Indumentaria o Comida): """)
        tam=os.path.getsize(aflocales)
        allocales.seek(tam)
        reglocal=pickle.load(allocales)
        reglocal.name = nomb
        reglocal.ubi = ubi
        reglocal.rubro = rubro
        desicion = input("¿Desea crear un nuevo local?(Si/No)")
        while desicion != "si" and desicion != "no":
         desicion = input("Ingrese opcion valida(Si/No)")

def modificar_locales(current_user, afUser, alUser):
    current_user.codeUs(afUser,alUser)
    flag1 = busquedaxbarrido_ModificarLocales(aflocales, allocales, current_user)
    if flag1 == True:
        name = input("Ingrese el nombre del local: ")
        validationName = busquedaxbarrido_NombreLocal(aflocales, allocales, name)
        flag4 = True
        intentosnom = 0
        while not validationName and flag4:
            name = input("Nombre ya existente, ingrese otro: ")
            validationName = busquedaxbarrido_NombreLocal(aflocales, allocales, name)
            intentosnom += 1
            if intentosnom = 3:
                flag4 = False
        ubi = input("Ingrese la unicacion del local: ")
        rubro = input("""Ingrese el rubro de su local (Disponibles : Perfumería, Indumentaria o Comida): """)
        rubro.lower()
        while rubro != "perfumeria" and rubro != "indumentaria" and rubro != "comida":
            rubro = input("""Su rubro no existe, ingrese otro (Perfumería, Indumentaria o Comida): """)
        tam=os.path.getsize(aflocales)
        allocales.seek(tam)
        reglocal=pickle.load(allocales)
        reglocal.name = name
        reglocal.ubi = ubi
        reglocal.rubro = rubro


    
def gestion_de_locales():
    sub_menu_admin()
    op = int(input("Ingrese que opción quiere realizar"))
    validar_op(op,"a","e")
    match op:
        case "a":
            crear_locales(aflocales,allocales)
        case "b":
            pass
        case "c":
            pass
        case "d":
            pass
        case "e":
            pass
        
        



# Validacion de la opcion a elegir
def validar_op(x,n1,n2):
    while x > n2 or x < n1:
        print("Ingrese una opción correcta")
        x = int(input("ingrese que opción quiere realizar "))

# Funcion que muestra los procesos del menu
def show_menu():
    menu()
    op = int(input("ingrese que opción quiere realizar "))
    validar_op(op, 1, 3)
    match op:
        case 1:
            validation = login(afUser, alUser)
            if validation[0]:
                current_user = validation[1]
                if current_user.user_type == "administrador":
                    menu_administrador()
                elif current_user.user_type == "cliente":
                    pass
                    
        case 2:
            signup(afUser=afUser, alUser=alUser, user_type="cliente")
        case 3:
            pass 

# Funcion para abrir los archivos logicos         
def open_file(path_file):
    if not os.path.exists(path_file):
        object = open(path_file, 'w+b')
    else:
        object = open(path_file, 'r+b')
    return object

# En caso de que no exita ningun el administrador, es decir, la primera vez que se inicia el programa, crae el administrador
def create_admin():
    alUser.seek(0)
    if os.path.getsize(afUser) == 0:
        admin = User()
        admin.codeUs = 1
        admin.email = "admin@shopping.com"
        admin.password = "12345"
        admin.user_type = "administrador"
        alUser.seek(0)
        pickle.dump(admin,alUser)
        return True

#PP:
global locales
afUser = "./USUARIOS.dat"
alUser = open_file(afUser)
aflocales ="./LOCALES.dat"
allocales = open_file(aflocales)
create_admin()

show_menu()

alUser.close()