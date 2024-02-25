
print("Búsqueda de Arreglo Multidimensional")
def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)
    return False, (-1, -1)

# Ejemplo:
matriz = [

    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Definir el valor a buscar en la matriz:
valor_a_buscar = int(input("Ingrese el valor a buscar en la matriz: "))

# Realizar la búsqueda en la matriz:
encontrado, posicion = buscar_en_matriz(matriz, valor_a_buscar)

# Mostrar el resultado de búsqueda:
if encontrado:
    print(f"Valor {valor_a_buscar} se encuentra en la posicion {posicion}.")
else:
    print(f"Valor {valor_a_buscar} no se encontro en la matriz.")