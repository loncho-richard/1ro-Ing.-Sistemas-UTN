import os
import pickle
import datetime
import getpass as get
from datetime import datetime
from colorama import Fore, Back, Style, init
from prettytable import PrettyTable


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
        self.dSemana = []*7     # int
        self.status = ""
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
    
def menu_client():
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
    a)Crear locales.
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

def dicotomica(array, valor):
    q = False
    ini = 0
    fin = 49
    while not q and ini < fin:
        med = (ini+fin) // 2
        if array[med].name == valor:
            q = True
        elif array[med].name > valor:
            ini = med + 1
        else:
            fin = med -1
    if q:
        return True
    else:
        return False

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
            user_validation = user_validation.ljust(100)
            alUser.seek(0)
            size = os.path.getsize(afUser)
            while flag2 == False and alUser.tell() < size:
                puntero = alUser.tell()
                user = pickle.load(alUser)
                if user.email == user_validation:
                    user_password = user.password
                    flag1 = True
                    flag2 = True
                    
        if count == 3:
            count += 1
            print("el usuario no existe \n Presiona enter para volver a intentarlo")
            input()
            return (False,)
        alUser.seek(puntero)
        if user.email == user_validation:
            password_validation = get.getpass("Ingresa la contraseña: ")
            password_validation = password_validation.ljust(100)
            if user_password == password_validation:
                return (True, user,)
                
            #
            else:
                count += 1
                print("La contraseña es incorrecta \n Presione enter para volver a intentarlo")
                input()

                if count == 3:
                    return (False,)

# Funcion por barrido para encontrar si existe o no le usuario
def busquedaxbarrido(email):
        aux = User()
        flag1 = False
        tam = os.path.getsize(afUser)
        alUser.seek(0)
        while alUser.tell() < tam and not flag1:
            aux = pickle.load(alUser)
            if aux.email == email:
                flag1= True
        if flag1:
            return False
        else:
            return True

#Buca y compara por medio de un barrido secuencial un código de usuario
def busquedaxbarrido_CodeDueno(cod):
        flag1 = False
        tam = os.path.getsize(aflocales)
        allocales.seek(0)
        while allocales.tell() < tam and not flag1:
            aux = pickle.load(allocales)
            if aux.codeUs == cod:
                if aux.user_type == "dueño de local":
                    flag1= True
        if flag1:
            return True
        else:
            return False

#Buca y compara por medio de un barrido secuencial un código de local
def busquedaxbarrido_ModificarLocales(cod):
        global allocales, aflocales
        flag1 = False
        tam = os.path.getsize(aflocales)
        allocales.seek(0)
        while allocales.tell() < tam and not flag1:
            aux = pickle.load(allocales)
            if aux.codeLocal == cod:
                flag1= True
        if flag1 == True:
            return True, aux
        else:
            return False,

#Buca y compara por medio de un barrido secuencial un nombre de local HAY QUE CAMBIAR ESTO
def busquedaxbarrido_NombreLocal(nom):
        flag1 = False
        tam = os.path.getsize(aflocales)
        allocales.seek(0)
        while allocales.tell() < tam and not flag1:
            aux = pickle.load(allocales)
            if aux.name == nom:
                flag1= True
        if flag1 == True:
            return True
        else:
            return False 
#Comprueba si existe el código de promoción y retorna el registro
def busquedaxbarrido_codPromo(cod):
    global alpromo, afpromo
    aux = Promo()
    flag1 = False
    tam = os.path.getsize(afpromo)
    alpromo.seek(0)
    while alpromo.tell() < tam and not flag1:
        aux = pickle.load(alpromo)
        if aux.codPromo == cod:
            flag1 = True
    if flag1:
        return True, aux
    else:
        return False, 0





def muestra_promocionesxDueno(code):
        aux = User()
        tam = os.path.getsize(aflocales)
        allocales.seek(0)
        while allocales.tell() < tam:
            aux = pickle.load(allocales)
            if aux.codeUs == code and aux.status =="A":
                tam2 = os.path.getsize(afpromo)
                alpromo.seek(0)
                while alpromo.tell() < tam2:
                    aux2 = pickle.load(alpromo)
                    if aux2.codeLocal == aux.codeLocal:
                        now = datetime.today()
                        if now >= aux2.fechaIniP and now <= aux2.fechaFinP:
                            print(f"Actualmente tiene una promoción que va desde {aux2.fechaIniP} hasta {aux2.fechaFinP}")
                            print(aux2.textpromo)
                            print(aux2.status)                          


# Funcion para crear Usuarios, dependiendo del "user_type", podemos crear un "cliente" o un "dueño local"
def signup(user_type):
    os.system("cls")
    flag2 = False
    existe = True
    email = obtener_input_con_limite("Email: ", 100)
    email = email.ljust(100)
    existe = busquedaxbarrido(email)
    while existe == False:
        print("Esta mail ya está ingresado, ingrese otro")
        email = obtener_input_con_limite("Email: ", 100)
        email = email.ljust(100)
        existe = busquedaxbarrido(email)

    while flag2 == False:
        password = obtener_input_con_limite("Contraseña: ", 8)
        re_password = obtener_input_con_limite("Repetir contraseña: ", 8)
        if password == re_password:
            flag2 = True
        else:
            print("Las contraseñas no coinciden, presiona enter para volver a intentarlo...")
            input()
    
    password = password.ljust(100)
    uid = busqueda_del_ultimo()
    uid += 1
    client = User()
    client.codeUs = uid
    client.email = email.ljust(100)
    client.password = password
    user_type = user_type.ljust(100)
    client.user_type = user_type
    size = os.path.getsize(afUser)
    alUser.seek(size)
    pickle.dump(client, alUser)
    alUser.flush()
    print(f"Has registrado este usuario correctamente, su código de usuario es {uid}")

# Funcion para buscar el ultimo id, y poder crear un id autoincrementable
def busqueda_del_ultimo():
    global alUser, afUser
    c = 0
    t = os.path.getsize(afUser)
    alUser.seek(0)
    while alUser.tell() < t:
        pickle.load(alUser)
        c +=1
    return c

# Input con limit, "maxlength"
def obtener_input_con_limite(prompt, limite):
    entrada = input(prompt)
    while len(entrada) > limite:
        print(f"La entrada debe tener como máximo {limite} caracteres.")
        entrada = input(prompt)
    return entrada


def busqueda_codlocal_coddueno(cod):
    flag1 = False
    tam = os.path.getsize(aflocales)
    allocales.seek(0)
    aux = Local()        
    while allocales.tell() < tam and not flag1:
            aux = pickle.load(allocales)
            if aux.codeLocal == cod:
                tam2 = os.path.getsize(afUser)
                alUser.seek(0)
                while alUser.tell() < tam2:
                    aux2 = pickle.load(alUser)
                    if aux.codeUs == aux2.codeUs: 
                        estado = "A".ljust(100)
                        if aux.status == estado:
                            flag1 = True
                            

    if flag1 == True:
        return True
    else:
        return False      

def busqueda_mayor_codpromo():
    global alpromo,afpromo
    tam = os.path.getsize(afpromo)
    alpromo.seek(0)
    aux = 0
    while alpromo.tell() < tam:
        reg = Promo()
        reg = pickle.load(alpromo)
        if reg.codPromo > aux:
            aux = reg.codPromo
    return aux

def crear_descuento(usuario):
    global alUser,alpromo,afUser
    usuario = User()
    muestra_promocionesxDueno(usuario.codeUs)
    cod = int(input("Ingrese el codigo del local en el cual desea crear el descuento: "))
    valido = busqueda_codlocal_coddueno(cod)
    contintentos = 0
    if  valido == False and contintentos != 2:
        cod = int(input("El codigo no pertenece a un local suyo o el local se encuentra inactivo, ingrese otro: "))
        valido = busqueda_codlocal_coddueno(cod)
        contintentos += 1
    if valido:
        descripcion = str(input("Ingrese un texto descriptivo de la oferta: "))
        descripcion = descripcion.ljust(100)
        mes1 = int(input("Ingrese el mes en que empezara a estar vigente la promocion  "))
        dia1 = int(input("Ingrese el dia en que empezará la promocion "))
        fecha1= datetime(2023,mes1,dia1, 12, 0, 0)
        hoy = datetime.today()
        cantin = 0
        while fecha1 < hoy and cantin != 3:
            print ("fecha invalida, ingrese una fecha posible: ")
            input("Presione una tecla para continuar: ")
            mes1 = int(input("ingrese el mes en que estara vigente la promocion  "))
            dia1 = int(input("Ingrese el dia en que empezará la promocion "))
            fecha1= datetime(2023,mes1,dia1, 12, 0, 0)
            cantin +=1
        mes2 = int(input("Ingrese el mes en que terminara de estar vigente la promocion  "))
        dia2 = int(input("Ingrese el dia en que termina la promoción "))
        fecha2 = datetime(2023,mes2,dia2, 12, 0, 0)
        cantin = 0
        while fecha1 > fecha2 and cantin != 3:
            print ("Fecha invalida, ingrese una fecha posible: ")
            input("Presione una tecla para continuar: ")
            mes2 = int(input("ingrese el mes en que dejara de estar vigente la promocion  "))
            dia2 = int(input("Ingrese el dia en que termina la promocion "))
            fecha2= datetime(2023,mes2,dia2, 12, 0, 0)
            cantin +=1
        dias = input("Desea que la promocion este disponible todos los dias (Lunes - Domingo) ")
        dias.lower()
        diasaprobados = [0]*7 
        if dias == "si":
            for i in range (7):
                diasaprobados[i] = 1
                
        else:
            for i in range (7):
                respuesta = input(f"Desea que la promocion este disponible el dia {i}?: (SI/NO) ")
                respuesta.lower()
                if respuesta == "si":
                    diasaprobados[i] = 1
                else:
                    diasaprobados[i] = 0
                    
        regpromo = Promo()
        alpromo.seek(0)
        tam = os.path.getsize(afpromo)
        status = "pendiente".ljust(100) 
          
        descripcion.ljust(100)
        regpromo.status = status
        regpromo.fechaIniP = fecha1
        regpromo.fechaFinP = fecha2         
        regpromo.codeLocal = cod
        regpromo.dSemana = diasaprobados
        regpromo.textPromo = descripcion
        alpromo.seek(tam)
        pickle.dump(regpromo,alpromo)
        alpromo.flush()

        

def reporte_descuentos():
    cantusos = 0
    mes1 = int(input("Ingrese desde que mes desea ver sus promociones(1-12): "))
    dia1= int(input("Ingrese desde que dia desea ver sus promociones: "))
    fechadesde= datetime(2023,mes1,dia1, 12, 0, 0)
    promos = [["None" for _ in range(5)] for _ in range(10)]
    hoy = datetime.today()
    cont = 0
    cantin = 0
    while fechadesde < hoy and cantin != 3:
        print ("fecha invalida, ingrese una fecha posible: ")
        input("Presione una tecla para continuar: ")
        mes1 = int(input("Ingrese desde que mes desea ver sus promociones   "))
        dia1 = int(input("Ingrese desde que dia desea ver sus promociones "))
        fechadesde= datetime(2023,mes1,dia1, 12, 0, 0)
        cantin +=1
    mes2 = int(input("Ingrese hasta cual mes quiere ver sus promociones(1-12): "))
    dia2 = int(input("Ingrese hasta que dia desea ver sus promociones "))
    fechahasta = datetime(2023,mes2,dia2, 12, 0, 0)
    cantin = 0
    while fechadesde > fechahasta and cantin != 3:
        print ("fecha invalida, ingrese una fecha posible: ")
        input("Presione una tecla para continuar: ")
        mes2 = int(input("Ingrese hasta que mes desea ver sus promociones:  "))
        dia2 = int(input("Ingrese hasta que dia desea ver sus promociones:  "))
        fechahasta= datetime(2023,mes2,dia2, 12, 0, 0)
        cantin +=1
    tam = os.path.getsize(afpromo)
    alpromo.seek(0)
    while alpromo.tell() < tam:
        regpromo = pickle.load(alpromo)
        if regpromo.fechaIniP <= fechadesde and regpromo.fechaFinP >= fechahasta:
            if regpromo.status == "aceptada".ljust(100):
                cont += 1
                tam2 = os.path.getsize(afusopromo)
                alusopromo.seek(0)
                flag9 = False
                while alusopromo.tell() < tam2 and not flag9:
                    regusoprom = pickle.load(alusopromo)
                    if regusoprom.codProm == regpromo.codProm:
                        if regusoprom.fechaUP >= fechadesde and regusoprom.fechaUP <= fechahasta:
                            cantusos +=1
                promos[cont][0] = [regpromo.codPromo]
                promos[cont][1] = [regpromo.textPromo]
                promos[cont][2] = [regpromo.fechaIniP]
                promos[cont][3] = [regpromo.fechaFinP]
                promos[cont][4] = [cantusos]

    tabla = PrettyTable()
    tabla.field_names = ['Codigo promocion','Texto','Fecha desde','Fecha hasta', 'cantidad de usos']
    for i in range(1,10):
        tabla.add_row([promos[i][0], promos[i][1], promos[i][2], promos[i][3], promos[i][4]])   
    print(tabla)        


#Busca la cantidad de locales que hay
def cantidad_locales():
    if os.path.getsize(aflocales) != 0:
        allocales.seek(0)
        pickle.load(allocales)
        un_reg = allocales.tell()
        tam = os.path.getsize(aflocales)
        cantidad_locales = tam // un_reg
        allocales.seek(0)
        return cantidad_locales
    else:
        return 0

def busqueda_nom_conCodLocal(code):
    flag1 = False
    tam = os.path.getsize(aflocales)
    allocales.seek(0)
    while allocales.tell() < tam and not flag1:
        aux = pickle.load(allocales)
        if aux.codeLocal == code:
            flag1 = True
            return aux.name


def Lista_negocios_pendientes():
    global alpromo, afpromo
    flag1 = False
    aux = Promo()
    tam = os.path.getsize(afpromo)
    if tam != 0:
        alpromo.seek(0)
        while alpromo.tell() < tam and not flag1:
            puntero = alpromo.tell()
            aux = pickle.load(alpromo)
            if aux.status == "pendiente".ljust(100):
                Nombre =busqueda_nom_conCodLocal(aux.codeLocal)
                print(f"el local {Nombre} con código de local {aux.codeLocal} tiene una solicitud pendiente:")
                print(f"""
                texto promo: {aux.textPromo}
                fecha inicio: {aux.fechaIniP}
                fecha finalización: {aux.fechaFinP}
                días de la semana:
                            Lunes: {aux.dSemana[0]}
                            Martes: {aux.dSemana[1]}
                            Miércoles: {aux.dSemana[2]}
                            Jueves: {aux.dSemana[3]}
                            Viernes: {aux.dSemana[4]}
                            Sábado: {aux.dSemana[5]}
                
------------------------------------------------------------------------------------------------------------------------""")
                flag1 = True
    if flag1:
        estado = str(input("Ingrese estado de solicitud: (aceptada/rechazada)"))
        codProm = int(input("Ingrese un código de promoción"))
        estado = estado.ljust(100)
        aux.status = estado
        aux.codPromo = codProm
        alpromo.seek(puntero)
        pickle.dump(aux, alpromo)
        alpromo.flush()
        
    if not flag1:
        print("Ningún local ha solicitado promociones")
    else:
        print("No hay promociones cargadas")


def aprobar_denegar_solicitudes():
    global afpromo, alpromo
    print("Estos son los negocios que solicitan descuentos:")
    Lista_negocios_pendientes()
    

    """class Promo():
    def __init__(self):
        self.codPromo = 0
        self.textPromo = ""
        self.fechaIniP = 0 
        self.fechaFinP = 0
        self.dSemana = []*6     # int
        self.status = ""
        self.codeLocal = 0
"""
def reporte_utilizacion_descuentos():
    global alpromo, afpromo

    mesini = int(input("Ingrese desde que mes desea ver sus promociones:  "))
    diaini = int(input("Ingrese desde que dia desea ver sus promociones:  "))
    fechaini = datetime(2023,mesini,diaini, 12, 0, 0)

    mesfi = int(input("Ingrese hasta que mes desea ver sus promociones:  "))
    diafi = int(input("Ingrese hasta que dia desea ver sus promociones:  "))
    fechafi = datetime(2023,mesfi,diafi, 12, 0, 0)

    alpromo.seek(0)
    tam = os.path.getsize(afpromo)
    while alpromo.tell() < tam:
        aux = pickle.load(alpromo)
        if fechaini >= aux.fechaIniP and fechafi <= aux.fechaFinP:
            if aux.status == "aceptada".ljust(100):
                print(f"Codigo: {aux.codPromo}\nDescripcion: {aux.textPromo}\nFecha inicial: {aux.fechaIniP}\nFecha final: {aux.fechaFinP}\nCodigo del local: {aux.codeLocal}")
            else:
                print("No hay promociones")

#crea locales, los almacena en el archivo correspondiente y muestra cantidad x rubros         
def crear_locales():
    global aflocales, allocales, alUser, afUser
    decision = input("¿Desea crear un local?(Si/No)")
    decision.lower()
    flag1 = False
    while decision != "si" and decision != "no":
        flag1 = False
        decision = input("Ingrese opcion valida(Si/No)")
        decision.lower()
    while decision == "si":   
        cant_locales = cantidad_locales()
        if cant_locales == 50:
            print("No hay mas espacio para cargar locales")
        else:
            nomb = input("Ingrese el nombre de su nuevo local: ")
            nomb = nomb.ljust(100)
            existenom = busquedaxbarrido_NombreLocal(nomb)
            intentosnom = 0
            while existenom and intentosnom < 2:
                nomb = input("Nombre ya existente, ingrese otro: ")
                nomb = nomb.ljust(100)
                existenom = busquedaxbarrido_NombreLocal(nomb)
                intentosnom += 1
            if intentosnom < 2 :
                ubi = input("Ingrese la ubicacion del local (por ejemplo ‘primer piso, ala este, sector B): ")
                ubi = ubi.ljust(100)
                cod = int(input("Ingrese su codigo de dueño de local:"))
                existecod = busquedaxbarrido_CodeDueno(cod)
                intentos = 0
                while existecod and intentos < 2:
                    cod = int(input("Su codigo de dueño de local no existe o no es de tipo dueño, ingrese otro:"))
                    existecod = busquedaxbarrido_CodeDueno(afUser,alUser,cod)
                    intentos += 1
                    if intentos == 2:
                        print("Has ingresado el código mal muchas veces")
                        flag1 = True
                        print("Los datos no han sido guardados, presione enter para realizarlo nuevamente")
                        input()
                if flag1 == False:
                    rubro = input("""Ingrese el rubro de su local (Disponibles : Perfumería, Indumentaria o Comida): """)
                    rubro.lower()
                    if rubro == "perfumería" or rubro == "indumentaria" or rubro == "comida":
                        flag1 == True
                    while rubro != "perfumeria" and rubro != "indumentaria" and rubro != "comida":
                        rubro = input("""Su rubro no existe, ingrese otro (Perfumería, Indumentaria o Comida): """)
                        rubro.lower()
                    rubro = rubro.ljust(100)
                    tam=os.path.getsize(aflocales)
                    allocales.seek(tam)
                    estado = "A".ljust(100)
                    reglocal = Local()
                    reglocal.name = nomb
                    reglocal.ubi = ubi
                    reglocal.rubro = rubro
                    reglocal.status = estado
                    codlocal = busqueda_mayor_codlocal() + 1
                    reglocal.codeLocal = codlocal
                    reglocal.codeUs = cod            
                    pickle.dump(reglocal,allocales)
                    allocales.flush()
                    print(f"Local guardado con éxito, su código de local es {codlocal}")
            
            decision = input("¿Desea crear un nuevo local?(Si/No)")
            decision.lower()
            while decision != "si" and decision != "no":
                decision = input("Ingrese opcion valida(Si/No)")
                decision.lower()
    mostrar_rubros()

#Busca el mayor(último) código de local
def busqueda_mayor_codlocal():
    global allocales,aflocales
    tam = os.path.getsize(aflocales)
    allocales.seek(0)
    aux = 0
    while allocales.tell() < tam:
        reg = Local()
        reg = pickle.load(allocales)
        if reg.codeLocal > aux:
            aux = reg.codeLocal
    return aux

#Usada en crear locales para mostrar la cantidad de locales x rubro
def mostrar_rubros():
    global allocales, aflocales

    indumentaria = "indumentaria".ljust(100)
    comida = "comida".ljust(100)
    perfumeria = "perfumeria".ljust(100)

    cont_indumentaria = 0 
    cont_perfumeria = 0
    cont_comida = 0
    allocales.seek(0)
    tam = os.path.getsize(aflocales)
    while allocales.tell() < tam:
        local = pickle.load(allocales)
        rubro = local.rubro
        if rubro == indumentaria:
            cont_indumentaria += 1
        if rubro == comida:
            cont_comida += 1
        if rubro == perfumeria:
            cont_perfumeria += 1

    rubros = [['indumentaria', cont_indumentaria], 
              ['comida', cont_comida], 
              ['perfumeria', cont_perfumeria]]
    col = 1
    for i in range (1):
        
        for k in range (i+1, 2):
            if rubros[i][col] > rubros[k][col]:
                for w in range(1):
                    aux = rubros[w][i]
                    rubros[i][w] = rubros[k][w]
                    rubros[k][w] = aux

    print(f"""
    La cantidad de locales de cada rubro es:
    {rubros[0][0]}: {rubros[0][1]}
    {rubros[1][0]}: {rubros[1][1]}
    {rubros[2][0]}: {rubros[2][1]} """)

#Modifica locales y los almacena nuevamente en el archivo correspondiente
def modificar_locales():
    global aflocales,allocales
    reglocal = Local()
    allocales.seek(0)
    pickle.load(allocales)
    Unreg = allocales.tell()
    codlocal = int(input("Ingrese el codigo de local que desea modificar: "))
    valido = busquedaxbarrido_ModificarLocales(codlocal)
    flag5 = True
    cont = 0
    while valido == False and flag5:
        codlocal = int(input("Ingrese un codigo de local existente: "))
        valido = busquedaxbarrido_ModificarLocales(codlocal)
        cont += 1
        if cont == 3:
            flag5 = False
            print("Superaste la cantidad de intentos, vuelva a intentarlo")
            input()
    if valido[0] == True:
        reglocal = valido[1]
        if reglocal.status == "B":
            q = input("Este local esta dado de baja, ¿Desea darlo de alta? 'Si/No' : ")
            q = q.lower()
            if q == "si":
                reglocal.status = "A"
        if reglocal.status == "A":
            if valido[0] == True:
                name = input("Ingrese el nuevo nombre del local : ")
                name = name.ljust(100)
                validationName = busquedaxbarrido_NombreLocal(name)
                flag4 = True
                intentosnom = 0
                while validationName and flag4:
                    name = input("Nombre ya existente, ingrese otro: ")
                    name = name.ljust(100)
                    validationName = busquedaxbarrido_NombreLocal(name)
                    intentosnom += 1
                    if intentosnom == 3:
                        flag4 = False
            ubi = input("Ingrese la ubicacion del local: ")
            ubi = ubi.ljust(100)
            rubro = input("""Ingrese el rubro de su local (Disponibles : Perfumería, Indumentaria o Comida): """)
            rubro.lower()
            while rubro != "perfumeria" and rubro != "indumentaria" and rubro != "comida":
                rubro = input("""Su rubro no existe, ingrese otro (Perfumería, Indumentaria o Comida): """)
                rubro.lower()
            rubro = rubro.ljust(100)
            reglocal.name = name
            reglocal.ubi = ubi
            reglocal.rubro = rubro
            puntero = allocales.tell()- Unreg
            allocales.seek(puntero)
            pickle.dump(reglocal,allocales)
            print("local modificado con éxito")
            
#Dar de baja lógica a un local HAY QUE MODIFICARLO
def eliminar_locales():
    global aflocales,allocales
    allocales.seek(0)
    pickle.load(allocales)
    Unreg = allocales.tell()
    reglocal = Local()
    codlocal= int(input("Ingrese el codigo de local: "))
    valido = busquedaxbarrido_ModificarLocales(codlocal)
    if valido[1].status == "B":
        print("El local ya está dado de baja")
    elif valido[0] == True:
        question = str(input("Estas seguro que deseas eliminar el local!? Si/No: "))
        question.lower()
        
        if question == "si":
            reglocal = valido[1]
            puntero = allocales.tell() - Unreg 
            allocales.seek(puntero)
            status = "B"
            reglocal.status = status
            pickle.dump(reglocal,allocales)
            allocales.flush()
            print("Local dado de baja con éxito")


def carga_locales_arreglo():
    global allocales, aflocales
    i = 0  
    locales = [[00 for _ in range(2)] for _ in range(50)]
    allocales.seek(0)
    tam = os.path.getsize(aflocales)
    while allocales.tell() < tam:
        i += 1
        local = pickle.load(allocales)
        locales[i][0] = local.codeLocal
        locales[i][1] = local.status

    return locales



def question(idx, status):

    if idx < 10:
        if status == "A".ljust(100):
            return Fore.GREEN + f"|O{idx}"
        else:
            return Fore.RED + f"|0{idx}"
    elif idx == 0:
        return Fore.WHITE + "|00"
    else:
        if status == "A".ljust(100):
            return Fore.GREEN + f"|{idx}"
        else:
            return Fore.RED + f"|{idx}"


def map_shops():
    db = carga_locales_arreglo()
    i = 0
    for floor in range(1):
        print(f"Piso {floor + 1}")
        for row in range(10):
            print("+--+--+--+--+--+")
            id_1 = db[i][0]
            status_1 = db[i][1]
            i += 1
            id_2 = db[i][0]
            status_2 = db[i][1]
            i += 1
            id_3 = db[i][0]
            status_3 = db[i][1]
            i += 1
            id_4 = db[i][0]
            status_4 = db[i][1]
            i += 1
            id_5 = db[i][0]
            status_5 = db[i][1]
            i += 1  
            print(f"{question(id_1, status_1)}{question(id_2, status_2)}{question(id_3, status_3)}{question(id_4, status_4)}{question(id_5, status_5)}|")
        
        print("+--+--+--+--+--+")
        print("     (...)      ")
        
#sub-menu de gestión de locales   
def gestion_de_locales():
    sub_menu_admin()
    op = input("Ingrese que opción quiere realizar ")
    validar_op(op,"a","e")
    while op != "e":
        match op:
            case "a":
                crear_locales()
            case "b":
                modificar_locales()
            case "c":
                eliminar_locales()
            case "d":
                map_shops()
                input()
        sub_menu_admin()
        op = input("Ingrese que opción quiere realizar ")
        validar_op(op,"a","e")
# Funcion que muestra los procesos del menu
def show_menu():
    menu()
    op = int(input("ingrese que opción quiere realizar "))
    validar_op(op, 1, 3)
    while op != 0:
        match op:
            case 1:
                validation = login(afUser, alUser)
                if validation[0]:
                    current_user = validation[1]
                    if current_user.user_type == "administrador".ljust(100):
                        menu_administrador()
                    dueno ="dueño".ljust(100) 
                    if current_user.user_type == dueno:
                        menu_dueno(current_user)
                    cliente = "cliente".ljust(100)
                    if current_user.user_type == cliente:
                        menu_cliente(current_user)
                        
            case 2:
                signup(user_type="cliente")
        menu()
        op = int(input("ingrese que opción quiere realizar  "))    

#Aprueba el uso de un código de descuento siempre y cuando sea válido
def solicitar_descuento(usuario):
    global afusopromo, alusopromo
    reg = Promo()
    cod = int(input("Ingrese el código de descuento que desea utilizar"))
    validation = busquedaxbarrido_codPromo(cod)
    reg = validation[1]
    print(validation[0])
    if  validation[0]:
        if reg.status == "aceptada".ljust(100):
            fecha = datetime.today()
            dia = datetime.today().weekday()
            if fecha > reg.fechaIniP and fecha < reg.fechaFinP:
                if reg.dsemana[dia] == 1:
                   ureg = Use_Promo()
                   ureg.codPromo = cod
                   ureg.fechaUP = fecha
                   ureg.codClient = usuario.codeUs
                   t = os.path.getsize(afusopromo)
                   alusopromo.seek(t)
                   pickle.dump(ureg, alusopromo)
                   print("Descuento usado con éxito")
                   input()
                else:
                    print("Hoy no está esa promoción válida")
                    input()
            else:
                print("Promoción expirada")
                input()  
        else:
            print("No se ha podido brindar el código, este código no está aprobado")
            input()
    else:
        print("No hay descuento valido con ese codigo")
        input()

def buscar_descuentos():
    codlocal = int(input("Ingrese un codigo de local para ver sus descuentos  "))
    mes1 = int(input("Ingrese el mes en que busca descuentos  "))
    dia1 = int(input("Ingrese el dia en que busca descuentos "))
    fecha = datetime(2023, mes1, dia1, 12, 0, 0)
    promos = [["" for _ in range(4)] for _ in range(10)]
    hoy = datetime.today()
    cont = 0
    cantin = 0
    while fecha < hoy and cantin != 3:
        print ("fecha invalida, ingrese una fecha posible: ")
        input("Presione una tecla para continuar: ")
        mes1 = int(input("Ingrese el mes en que busca descuentos  "))
        dia1 = int(input("Ingrese el dia en que busca descuentos "))
        fecha= datetime(2023, mes1, dia1, 12, 0, 0)
        cantin +=1
    diasemana = datetime(2023, mes1, dia1, 12, 0, 0).weekday()
    tam = os.path.getsize(afpromo)
    alpromo.seek(0)
    while alpromo.tell() < tam:
        regpromo = pickle.load(alpromo)
        if codlocal == regpromo.codeLocal:
            if regpromo.fechaIniP <= fecha and regpromo.fechaFinP >= fecha:
                if regpromo.status == "aceptada".ljust(100):
                    if regpromo.dSemana[diasemana] == 1:
                        cont += 1
                        promos[cont][0] = [regpromo.codPromo]
                        promos[cont][1] = [regpromo.textPromo]
                        promos[cont][2] = [regpromo.fechaIniP]
                        promos[cont][3] = [regpromo.fechaFinP]
    tabla = PrettyTable()
    tabla.field_names = ['Codigo promocion','Texto','Fecha desde','Fecha hasta']
    for i in range(1,10):
        tabla.add_row([promos[i][0], promos[i][1], promos[i][2], promos[i][3]])   
    print(tabla)        
    

#sub-menu de usuario del tipo cliente
def menu_cliente(usuario):
    menu_client()
    op = int(input("Ingrese que opción quiere realizar "))
    validar_op(op,0,3)
    while op != 0:
        match op:
            case 1:
                buscar_descuentos()
            case 2:
                solicitar_descuento(usuario)
        menu_client()
        op = int(input("Ingrese que opción quiere realizar "))
        validar_op(op,0,3)
        
                
#menu en caso de que el usuario sea del tipo dueño de local
def menu_dueno(usuario):
    menu_owner()
    op = int(input("Ingrese la opcion que desee realizar: "))
    validar_op(op,0,3)
    while op != 0:
        match op:
            case 1:
                crear_descuento(usuario)
            case 2:
                reporte_descuentos()
        menu_owner()
        op = int(input("Ingrese la opcion que desee realizar: "))
        validar_op(op,0,3)

#Menu en caso de que el usuario sea del tipo administrador
def menu_administrador():
    menu_admin()
    op = int(input("ingrese que opción quiere realizar: "))
    validar_op(op,0,5)
    while op != 0:
        match op:
            case 1:
                gestion_de_locales()
            case 2:
                signup(user_type="dueño")
            case 3:
                aprobar_denegar_solicitudes()
            case 4:
                print("Diagramado en Chapin")
            case 5:
                reporte_utilizacion_descuentos()
        menu_admin()
        op = int(input("ingrese que opción quiere realizar: "))

# En caso de que no exista ningun el administrador, es decir, la primera vez que se inicia el programa, crea el administrador
def create_admin():
    alUser.seek(0)
    if os.path.getsize(afUser) == 0:
        admin = User()
        admin.codeUs = 1
        admin.email = "admin@shopping.com"
        admin.email = admin.email.ljust(100)
        admin.password = "12345"
        admin.password = admin.password.ljust(100)
        admin.user_type = "administrador"
        admin.user_type = admin.user_type.ljust(100)
        pickle.dump(admin,alUser)
        alUser.flush()
        return True

# Validacion de la opcion a elegir
def validar_op(x,n1,n2):
    while x > n2 or x < n1:
        print("Ingrese una opción correcta")
        x = int(input("ingrese que opción quiere realizar "))

# Funcion para abrir los archivos logicos         
def open_file(path_file):
    if not os.path.exists(path_file):
        object = open(path_file, 'w+b')
    else:
        object = open(path_file, 'r+b')
    return object

#PP:
#Arreglo global

init(autoreset=True)

Locales = ["z"]*50

afUser = "./USUARIOS.dat"
alUser = open_file(afUser)
aflocales ="./LOCALES.dat"
allocales = open_file(aflocales)
afpromo = "./PROMO.dat"
afusopromo = "./USOPROMO.dat"
alusopromo = open_file(afusopromo)

alpromo = open_file(afpromo)

create_admin()
show_menu()

alUser.close()