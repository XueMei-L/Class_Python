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

# # Ejemplo matriz2
# print("Ejemplo 2:")
# matriz2 = [
#     [6,4,5],
#     [9,10,7]
# ]

# # imprimir el valor en la posición [1][1]
# print(matriz2[1][1])

# # imprimir una fila completa, por ejemlo fila 0
# print(matriz2[0])

# # imprimir una columna completa, por ejemplo columa 0
# columna = [matriz2[i][0] for i in range (len(matriz2))]

# print(columna)

# # Ejemplo matriz3 3 X 3
# print("Ejemplo 3:")
# matriz3 = [
#     [6,4,5],
#     [9,10,7],
#     [1,2,1],
# ]
# # Recorrer una matriz con sus índices
# print("Recorrer la matriz con sus índices usando for")
# for i in range(len(matriz3)): # fila 0 - fila 1 - fila 2
#     for j in range(len(matriz3[i])): # recorrer la posicion 0, 1, 2... en la fila i
#         print(matriz3[i][j])


# print("Recorrer una matriz con sus valores de usando for each")
# for fila in matriz3:
#     for elemento in fila:
#         print(elemento)

# Tarea 1: 05/12/2025
# Pedir al usuario una matriz de  3 X 3
# Introducir valores columna por columna utilizando el bucle for con los indices de la matriz y al final imprimirla por pantalla,
# es decir:
# Las siguientes son las iteraciones, pediré una modificación la proxima semana sobre el código, compartiendo la pantalla
# [2,]
# [4,]
# [6,]
# [2, 3]
# [4, 6]
# [6, 9]
# [2, 0, 0]
# [0, 2, 0]
# [0, 0, 2]

# n=int(input("Ingrese el número de filas de la matriz: "))
# m=int(input("Ingrese el número de columnas de la matriz: "))

# print("Es una matriz de",n,"x",m)

# matriz=[]
# for i in range(n):
#     fila=[]
#     for j in range(m):
#         valor=int(input(f"valor [{i}][{j}]: "))
#         fila.append(valor)
#     matriz.append(fila)

# print(matriz)



# matriz = [[2, 0, 0],
#           [0, 2, 0],
#           [0, 0, 2]]

# # reemplazar una posición concreta
# matriz[0][0] = 3
# matriz[1][1] = 3
# matriz[2][2] = 3

# print(matriz)


# # reemplazar fila entera
# matriz[0] = [1,2,3]

# print(matriz)

# # Insertar una nueva fila
# matriz.insert(1, [2,2,2])

# print(matriz)


# # Eliminar una fila entera
# matriz.pop(3)

# print(matriz)

# Matriz traspuesta
# Paso 1: Obtener una matriz
# matrizT = [
#     [6,4,5],
#     [9,10,7],
#     [1,2,1],
# ]

# # Paso 2: Obtener N de filas y M de columnas
# filas = len(matrizT)
# columnas = len(matrizT[0])

# # Paso 3: Crear una matriz vacia de M filas y N columnas - coger filas X columnas, convertir en el tamaño de columnas X filas
# matrizR = [[0 for _ in range(filas)] for _ in range(columnas)]

# # Paso 4: Voy a recorrer mi matrizT, cambiar sus filas en columnas
# for i in range(filas):
#     for j in range(columnas):
#         matrizR[j][i] = matrizT[i][j]

# # Paso 5: Imprimir el matrizR
# for fila in matrizR:
#     print(fila)


# Tarea A:

# MatrizA = [
#     [1,1,1],
#     [2,2,2],
#     [3,3,3],
# ]

# MatrizB = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# Paso 1: Imprimir dos matrices

# Paso 2: Hacer la transpuesta de la matriz A y la matriz B - imprimir los resultados

# Paso 3: Hacer la suma de dos matrices - imprimir el resultado de la suma


# matriz = [
#     [3, 12, 1],
#     [5, 7, 9],
#     [0, 4, 6]
# ]

# # encontrar el mayor numero de una matriz
# mayor = matriz[0][0]

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if(matriz[i][j] > mayor):
#             mayor = matriz[i][j]
        
# print("El valor mayor: ", mayor)


# # contar cuantos valores pares hay en la matriz
# contador = 0

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if matriz[i][j] % 2 == 0:
#             contador += 1

# print("Cantidad de numeros pares", contador)

# # Imprimir el diagonal principal de una matriz
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         if i == j:
#             print(matriz[i][j])

# Tarea: imprimir el diagonal inversa


# matriz = [
#             [1,2],
#             [2,1],
# ]

# # len(matriz) -> tamaño de la fila
# # len(matriz[0]) -> tamaño de la columna

# if(len(matriz) == len(matriz[0])):
#     print("Es una matriz cuadrada")


# Imprimir el resultado de la suma de cada fila de una matriz

# matriz = [  [1,2,-3],
#             [4,-5,6],
#             [-7,8,9]
# ]

# suma = 0

# for fila in range(len(matriz)):
#     # fila = 0
#     # fila = 1
#     suma = 0

#     for columna in range(len(matriz[0])):
#         # columna = 0
#         # columna = 1
#         # columna = 2

#         # matriz[0][0] -> matriz[fila][columna]
#         suma += matriz[fila][columna]
#     print("suma de la fila", fila, "es igual a ", suma)
    

# Reemplazar los numeros que sean divisores de 15 a un 0
# matriz = [  [5,1,3],
#             [15,2,6],
#             [1,7,9],
# ]

# for fila in range(len(matriz)):
#     for columna in range(len(matriz[0])):
#         if(matriz[fila][columna] != 0):
#             if(15 % matriz[fila][columna] == 0):
#                 matriz[fila][columna] = 0
#                 print("es divisor de 15, reemplazar el valor")

# print(matriz)


# Tarea 1: contar cuantos 0 hay en una matriz de 5x5
# matrix = [  [1, 2, 1, 1, 0],
#             [0, 1, 0, 0, 1],
#             [1, 0, 2, 0, 0],
#             [1, 2, 0, 1, 2],
#             [0, 2, 1, 0, 1] ]

# contador=0

# for i in range (len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]==0:
#             contador+=1
# print("cantidad de números 0 es", contador)

# Tarea 1: calcular la nota media de cada alumno (nota media = la suma de cada fila/numero de notas), 
# agrupa estos nuevos alumnos en las clases diferentes:
# si es superior que 90: A
# si es inferior que 90, pero es superor que 70: B  
# si es inferior que 70, pero es superior que 50: C
# si es inferior que 50: D
# imprime el resultado cada clase. A,B,C,D

# notas = [
#     [85, 92, 78, 88, 95],   # alumno1
#     [67, 88, 95, 72, 81],   # alumno2
#     [99, 79, 88, 93, 89],   # alumno3
#     [45, 52, 61, 58, 49],   # alumno4
#     [77, 82, 90, 50, 42],   # alumno5
#     [95, 98, 91, 96, 93],   # alumno6
#     [25, 33, 77, 24, 41],   # alumno7
#     [72, 65, 78, 74, 69],   # alumno8
#     [43, 90, 33, 60, 32],   # alumno9
#     [59, 62, 55, 61, 58],]   # alumno10

# suma = 0
# ESO_01 = {
#     "A":{},
#     "B":{},
#     "C":{},
#     "D":{},
# }

# for fila in range (len(notas)):
#     suma = 0
#     for columna in range(len(notas[0])):
#         suma = suma + notas[fila][columna]
#     nota_media = suma / len(notas[0])
#     if(nota_media > 90):
#         ESO_01["A"][fila] = nota_media
#     if(nota_media < 90 and nota_media > 70):
#         ESO_01["B"][fila] = nota_media
#     if(nota_media < 70 and nota_media > 50):
#         ESO_01["C"][fila] = nota_media
#     else:
#         ESO_01["D"][fila] = nota_media

# print(ESO_01)

# Multiplicacion de matriz

# 2 X 3
matrizA = [ [2, 3, 5],
            [7, 2, 4],]

# 3 X 2
matrizB = [ [1, 6],
            [7, 2],
            [0, -5],]
# paso 1: comprobar que el tamaño del numero de la fila de matrizA coincide con el numero de la columna de matrizB
if(len(matrizA[0]) == len(matrizB)):
    print("Se puede realizar la multiplicación")
    # paso2: codigo de crear una matriz final
    matrizC = [[0 for _ in range(len(matrizA))] for _ in range(len(matrizB[0]))]
    print(len(matrizA))
    print(len(matrizB[0]))
else:
    print("No se puede realizar la multiplicación.")

# paso 3: recorrer dos matrices
for i in range(len(matrizA)):  # fila de A
    for j in range(len(matrizB[0])):  # columna de A && fila de B
        # matrizC[i][j] = 0
        for k in range(len(matrizB)):   # columna de B
            matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
print(matrizC)



# Un programa con varias funciones
# 1. Mostrar las matrices // hay 3 matrices, 
# 2. Mostrar las matrices traspuestas
# 3. Mostrar la suma de dos matrices // 1,2
# 4. Mostrar la multiplicacion de dos matrices // 1 3
