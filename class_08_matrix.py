# Matriz
# ¿Qué es una matriz?
# Matriz se forma con N filas y M columnas [ N Y M son números enteros positivos ]
# Matriz es una lista de listas

# Ejemplos de matrices
matriz1 = [1,2,3]  # 1 x 3 ->  1 fila y 3 columnas

matriz2 = [[1,1],[2,2]] # 2 x 2 -> 2 filas y 2 columnas

matriz3 = [[1, 2, 3], [4, 5, 6]] # 2 x 3 -> 2 filas y 3 columnas

# Crear matriz
# crear una matriz manualmente
matriz4 = [[2,3],[4,5]]
print(matriz4)

# crear una matriz vacía
matriz5 = []
print(matriz5)

# crear una matriz con valor 0
filas = 3
columnas = 3
matriz6 = [[0 for _ in range(columnas)] for _ in range(filas)]
# crear una fila con m columnas
# cada columna tiene el valor 0
# _ significa = el nombre de variable

print(matriz6)





