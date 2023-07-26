
def order(db,column,limit):
 for i in range(0,limit-1):
    for k in range(i+1,limit):
      if db[i][column] < db[k][column]:
        for w in range(colums):
            aux=db[i][w]
            db[i][w]=db[k][w]
            db[k][w]=aux
        
     
    
def save_in_db(db,column,line):
    global i
    nombre=str(input("ingrese el nombre "))
    repe=search(db,nombre,column,line)
    db[i][column]=nombre
    if repe == 1:
        nombre=str(input("nombre ya existente , ingrese otro "))
        db[i][column]=nombre
 
    i+=1
    order(db,column,line)
    return db
 
 

        

def search(db,obj,col,longi):
    q=False
    comi = 0
    fin = longi - 1
    for k in range(0,longi):
        while not (comi > fin or q):
            medio = (comi + fin)//2
            if obj == db[medio][col]:
                q=True
            elif obj < db[medio][col]:
                fin = medio-1
            else:
                comi=medio+1
            if q:
                return 1
            else:
                return 0
            
i=0
limite=0
filas=5
colums=3
shops=[0]*filas
for g in range(filas):
    shops[g]=[""]*colums
def crearlocales():
    global limite, filas, colums, shops, i

    opcion=int(input("seleccione lo que quiere: 1-cargar un nombre, 2-salir "))
    if (opcion == 1) and (limite < filas):
        limite= limite + 1
        arreglo = save_in_db(shops,0,filas)
    print (arreglo)





accion=int(input("quiere crear locales o no? 1-si 2-no 3-salir "))
while accion != 3:
    if accion == 1:
        crearlocales()
    accion=int(input("quiere crear locales o no? 1-si 2-no 3-salir "))