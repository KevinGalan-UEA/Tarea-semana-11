def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición si encuentra el valor
    return None  # Retorna None si no encuentra el valor

# Matriz 3x3 de ejemplo
matriz = [
    [5, 8, 3],
    [2, 9, 4],
    [7, 6, 1]
]

# Valor a buscar
valor_buscado = int(input("Ingresa el valor a buscar: "))

# Búsqueda del valor en la matriz
resultado = buscar_valor(matriz, valor_buscado)

# Mostrar resultados
if resultado:
    print(f"Valor encontrado en la posición: {resultado}")
else:
    print("Valor no encontrado en la matriz.")