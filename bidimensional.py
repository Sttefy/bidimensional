def buscar_en_matriz(matriz, elemento):
    """
    Función para buscar un elemento en una matriz bidimensional.
    Devuelve la posición del elemento si se encuentra, o None si no está presente.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                return (i, j)
    return None


matriz = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

elemento_a_buscar = int(input("Ingrese el número a buscar en la matriz: "))


resultado = buscar_en_matriz(matriz, elemento_a_buscar)


if resultado:
    print(f"El elemento {elemento_a_buscar} se encuentra en la posición: {resultado}")
else:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la matriz.")