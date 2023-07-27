def busqueda_por_corrimiento(arreglo, id_objetivo):
    for idx, fila in enumerate(arreglo):
        if fila[0] == id_objetivo:
            return idx

    return None

db = [[1, 'asd'],
      [2, 'asd'],
      [4, 'asd'],
      [6, 'asd'],
      [8, 'asd']]

idx = busqueda_por_corrimiento(db, 4)

print(type(idx), idx)