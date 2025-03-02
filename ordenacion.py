def bubble_sort(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de elementos


def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        print("Matriz original:")
        for fila in matriz:
            print(fila)

        # Ordenar la fila seleccionada
        bubble_sort(matriz[fila_index])

        print("\nMatriz con la fila ordenada:")
        for fila in matriz:
            print(fila)
    else:
        print("Índice de fila fuera de rango.")


# Matriz 3x3 de ejemplo
matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 6, 1]
]

# Elegir fila a ordenar
fila_a_ordenar = int(input("Ingresa el índice de la fila a ordenar (0-2): "))

# Ordenar la fila y mostrar resultados
ordenar_fila(matriz, fila_a_ordenar)