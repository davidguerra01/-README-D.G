print("Ordenación de Arreglo Multidimensional")
def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

def ordenar_fila_matriz(matriz, fila):
    bubble_sort(matriz[fila])
    return matriz

# Ejemplo:
matriz = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

fila_a_ordenar = 1  # Ordenamos la primera fila

print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila_matriz(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)