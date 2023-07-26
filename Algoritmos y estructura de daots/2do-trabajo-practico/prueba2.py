def busqueda_dicotomica_vertical_por_nombre(arreglo, nombre_objetivo):
    if not arreglo:
        return None

    filas = len(arreglo)
    izquierda = 0
    derecha = filas - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        nombre_medio = arreglo[medio][1]

        if nombre_medio == nombre_objetivo:
            return arreglo[medio][0]
        elif nombre_medio > nombre_objetivo:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return None

# Ejemplo de uso:
arreglo_datos = [
    [101, 'Alice'],
    [201, 'Bob'],
    [305, 'John'],
    [402, 'Mike'],
    [510, 'Sarah'],
    [600, 'Zoe']
]
nombre_buscado = 'Bob'

id_encontrado = busqueda_dicotomica_vertical_por_nombre(arreglo_datos, nombre_buscado)

if id_encontrado is not None:
    print(f"El ID para el nombre '{nombre_buscado}' es {id_encontrado}.")
else:
    print(f"No se encontró ningún ID para el nombre '{nombre_buscado}'.")