# # Matriz
# # ¿Qué es una matriz?
# # Matriz se forma con N filas y M columnas [ N Y M son números enteros positivos ]
# # Matriz es una lista de listas

# # Ejemplos de matrices
# matriz1 = [1,2,3]  # 1 x 3 ->  1 fila y 3 columnas

# matriz2 = [[1,1],[2,2]] # 2 x 2 -> 2 filas y 2 columnas

# matriz3 = [[1, 2, 3], [4, 5, 6]] # 2 x 3 -> 2 filas y 3 columnas

# # Crear matriz
# # crear una matriz manualmente
# matriz4 = [[2,3],[4,5]]
# print(matriz4)

# # crear una matriz vacía
# matriz5 = []
# print(matriz5)

# # crear una matriz con valor 0
# filas = 3
# columnas = 3
# matriz6 = [[0 for _ in range(columnas)] for _ in range(filas)]
# # crear una fila con m columnas
# # cada columna tiene el valor 0
# # _ significa = el nombre de variable
# print(matriz6)

# # Tarea1: Escribe una matrizA manualmente del tamaño 3 X 2 con números de 1 hasta 6
# matrizA = [[1, 2], [3, 4], [5, 6]]

# # Tarea2: Contesta la siguiente pregunta: Dime qué número es la posición [2][2] de la matrizA anterior y la posición [1][0]
# # Posición [2][2] sería un error (índice fuera de rango). Posición [2][1] = 6, Posición [1][0] = 3

# # Tarea3: Pedir al usuario N filas y M columas de una matriz, y crear una matriz de N filas y M columnas con valor 0, y imprimirl
# filas = int(input("Ingrese el número de filas: "))
# columnas = int(input("Ingrese el número de columnas: "))
# matriz7 = [[0 for _ in range(columnas)] for _ in range(filas)]


# -------------------------------------------------------------------------------------------

# Matriz con datos introducidos por el usuario
# print("Ejemplo 1:")
# matriz1 = [[6,4,5],[9,10,7]]   2 X 3
# [[6, 4], [5, 9], [10, 7]] 3 x 2

# N = int(input("Introduzca el número de la fila:"))
# M = int(input("Introduzca el número de la columna:"))

# print("Es una matriz de", N, " X ", M)

# matriz = []
# for i in range(N):
#     fila = []
#     for j in range(M):
#         valor = int(input(f"Valor en la posición [{i},{j}]: "))
#         fila.append(valor)
#     matriz.append(fila)

# print(matriz)

# Ejemplo matriz2
print("Ejemplo 2:")
matriz2 = [
    [6,4,5],
    [9,10,7]
]

# imprimir el valor en la posición [1][1]
print(matriz2[1][1])

# imprimir una fila completa, por ejemlo fila 0
print(matriz2[0])

# imprimir una columna completa, por ejemplo columa 0
columna = [matriz2[i][0] for i in range (len(matriz2))]

print(columna)

# Ejemplo matriz3 3 X 3
print("Ejemplo 3:")
matriz3 = [
    [6,4,5],
    [9,10,7],
    [1,2,1],
]
# Recorrer una matriz con sus índices
print("Recorrer la matriz con sus índices usando for")
for i in range(len(matriz3)): # fila 0 - fila 1 - fila 2
    for j in range(len(matriz3[i])): # recorrer la posicion 0, 1, 2... en la fila i
        print(matriz3[i][j])


print("Recorrer una matriz con sus valores de usando for each")
for fila in matriz3:
    for elemento in fila:
        print(elemento)

