# Un programa con varias funciones
# 1. vamos al pedir usuario, número de matriz, y fila y columna
# 1. Mostrar las matrices // hay 3 matrices, 
# 2. Mostrar las matrices traspuestas
# 3. Mostrar la suma de dos matrices // 1,2
# 4. Mostrar la multiplicacion de dos matrices // 1 3


# Imprimir todas las matrices
def showAllMatrix():
    for name, matrix in matrixDictionary.items():
        print(name)
        print(matrix)


# Imprimir una matriz seleccionada
def showAMatrix(name):
    # comprobar que existe la matriz en el diccionario
    if name not in matrixDictionary:
        print("La matriz no existe")
        return
    
    # encontrar la Matriz en el diccionario
    matrix = matrixDictionary[name]

    # imprimir la matriz
    for i in range(len(matrix)):
        print("[", end=" ")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=", ")
        print("]")


def createMatrix(fila, columna):
    print("Crear una matrix nueva")
    # crear una matriz vacia con 0
    matrix = [[0 for _ in range(columna)] for _ in range(fila)]
    
    # recorrer cada posición para sustituir.
    for i in range(fila):
        for j in range(columna):
            valor = int(input(f"Valor en la posición [{i}][{j}]: "))
            matrix[i][j] = valor
    
    # poner más bonito
    print(matrix)
    name = "matrix" + str(len(matrixDictionary)+1)
    print(name)
    matrixDictionary[name] = matrix


def renameMatrices():
    # crear una nueva diccionario
    matrices = {}

    # empieza con la matriz 1
    contador = 1

    # recorrer el diccionario
    for _ , matrix in matrixDictionary.items():
        newName = "matrix" + contador
        matrices[newName] = matrix
        contador += 1

    matrixDictionary.clear()
    matrixDictionary.update(matrices)


def deleteMatrix(name):
    if name not in matrixDictionary:
        print("La matriz no existe, no se puede eliminar")
        return

    del matrixDictionary[name]
    print("Matriz eliminada")

    # renombrar todas las matrices
    renameMatrices()
    print("Renombramos todas las matrices")



# Mostrar la matrix traspuesta
def showTranspose(name):
    if name not in matrixDictionary:
        print("La matriz no existe")
        return
    
    matrix = matrixDictionary[name]

    # mostrar la traspuesta
    # Obtener N de filas y M de columnas
    filas = len(matrix)
    columnas = len(matrix[0])

    # Crear una matriz vacia de M filas y N columnas - coger filas X columnas, convertir en el tamaño de columnas X filas
    matrixT = [[0 for _ in range(filas)] for _ in range(columnas)]

    # Voy a recorrer mi matrixT, cambiar sus filas en columnas
    for i in range(filas):
        for j in range(columnas):
            matrixT[j][i] = matrix[i][j]

    # Imprimir el matrixT
    for fila in matrixT:
        print(fila)


def sumOfMatrix(name1, name2):
    # comprobar que dos matrices están en el diccionario
    if name1 not in matrixDictionary or name2 not in matrixDictionary:
        print("alguna matriz no existe")
        return

    matrix1 = matrixDictionary[name1]
    matrix2 = matrixDictionary[name2]

    # comprobar las dimensiones sean iguales
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("No se pueden realizar la suma, puesto que las dimensiones son distintas.")
        return
    
    # crar una matriz vacia para guardar el resultado de la suma - columnas - filas
    addMatrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            addMatrix[i][j] = matrix1[i][j] + matrix2[i][j]
    
    print("Imprimir la suma:")
    for i in range(len(addMatrix)):
        print("[", end=" ")
        for j in range(len(addMatrix[i])):
            print(addMatrix[i][j], end=", ")
        print("]")


def multiplyOfMatrix(name1,name2):
    # comprobar que dos matrices están en el diccionario
    if name1 not in matrixDictionary or name2 not in matrixDictionary:
        print("alguna matriz no existe")
        return
    
    matrix1 = matrixDictionary[name1]
    matrix2 = matrixDictionary[name2]
    # comando para replicar la linea entera: alt + shift + arriba / abajo
    if(len(matrix1[0]) != len(matrix2)):
        print("no se pueden realizar la multiplicacion, puesto que N filas de matrizA no coincide con N columna de matrixB.")
        return

    # crear una nueva matriz para guardar el resultado de la multiplicacion
    # columnas de B y filas de A
    multiplyMatrix = [[0 for _ in range(len(matrix1))] for _ in range(len(matrix2[0]))]

    # paso 3: recorrer dos matrices
    for i in range(len(matrix1)):  # fila de A
        for j in range(len(matrix2[0])):  # columna de A && fila de B
            # matrizC[i][j] = 0
            for k in range(len(matrix2)):   # columna de B
                multiplyMatrix[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print("Imprimir la multiplicacion:")
    for i in range(len(multiplyMatrix)):
        print("[", end=" ")
        for j in range(len(multiplyMatrix[i])):
            print(multiplyMatrix[i][j], end=", ")
        print("]")




# 2 X 3
matrix1 = [ [2, 3, 5],
            [7, 2, 4],]

matrix2 = [ [1, 1, 1],
            [2, 2, 2],]

# 3 X 2
matrix3 = [ [1, 6],
            [7, 2],
            [0, -5],]

# 2 x 3
matrix4 = [
    [2, 3, 5],
    [7, 2, 4]
]

# 3 x 2
matrix5 = [
    [1, 6],
    [7, 2],
    [0, -5]
]

# matrix diccionario
matrixDictionary = {}

def main():
    matrixDictionary["matrix1"] = matrix1
    matrixDictionary["matrix2"] = matrix2
    matrixDictionary["matrix3"] = matrix3
    matrixDictionary["matrix4"] = matrix4
    matrixDictionary["matrix5"] = matrix5

    # print(matrixDictionary)

    while True:
        print("----------------------Bienvenido al sistema de gestion del edificio----------------------")
        print("1. Mostrar todas las matrices")
        print("2. Mostrar una matriz seleccionada")
        print("3. Crear una nueva matriz")
        print("4. Eliminar una matriz")
        print("5. Mostrar la traspuesta de una matriz")
        print("6. Mostrar la suma de dos matrices")
        print("7. Mostrar la multiplicacion de dos matrices")

        print("0. Salir")

        opcion = int(input("\nSeleccione una opción: "))

        match opcion:
            case 1:
                print("Imrpimiendo todas las matrices...")
                showAllMatrix()
            
            case 2:
                # Mostrar solo los nombres
                for name in matrixDictionary:
                    print(name)
                
                # preguntar al usuario qué matriz quiere imprimir
                matrix = input("Elige la matriz que quieres imprimr: ")
                showAMatrix(matrix)
            
            case 3:
                fila = int(input("Introduzca el número de la fila: "))
                columna = int(input("Introduzca el número de la columna: "))
                createMatrix(fila, columna)
            
            case 4:
                # Mostrar solo los nombres
                for name in matrixDictionary:
                    print(name)
                
                print("Eliminar una matriz seleccionada")
                matrix = input("Elige la matriz que quieres eliminar")
                deleteMatrix(matrix)
            
            case 5:
                # Mostrar solo los nombres
                for name in matrixDictionary:
                    print(name)
                # preguntar al usuario la matriz traspuesta
                matrix = input("Elige la matriz que quieres mostrar la traspuesta:")
                showTranspose(matrix)
            
            case 6:
                showAllMatrix()
                # elegir nombre solo !
                matrixA = input("Elige la matriz A para sumar: ")
                matrixB = input("Elige la matriz B para sumar: ")
                sumOfMatrix(matrixA, matrixB)

            case 7:
                showAllMatrix()
                # elegir matrices con su nombre solo !
                matrixA = input("Elige la matriz A para multiplicacion: ")
                matrixB = input("Elige la matriz B para multiplicacion: ")
                multiplyOfMatrix(matrixA, matrixB)

                matrizA = "matriz04"
            case 0:
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida, inténtelo de nuevo.\n")

# forma de ejecutar el script
if __name__ == "__main__":
    main()







# matrix2=[[1,6],
#          [7,2],
#          [0,-5],]
# matrix1=[[2,3,5],
#          [7,2,4],]
# matriz= [
#      [1,2],
#      [2,1],]
# filas=len(matriz)
# columnas=len(matriz[0])
# matriz7=[[0 for j in range(filas)] for i in range(columnas)]
# #2 Mostrar las matrices traspuestas
# for i in range(filas):
#     for j in range(columnas):
#        matriz7[j][i]=matriz[i][j]
# for fila in matriz7:
#     print(fila)
# #3 suma de las matrices
# opcion = int(input("Elige una opción (1 o 2): "))
# if opcion ==1:
#     suma=0
#     for fila in range(len(matrix2)):
#         for columnas in range(len(matrix2[0])):
#             suma+=matrix2[fila][columnas]
# print("la suma de las fila", fila," es igual a", suma)
# if opcion ==2:
#     suma=0
#     for fila in range(len(matrix1)):
#         for columnas in range(len(matrix1[0])):
#             suma+=matrix1[fila][columnas]
# print("la suma de las fila", fila," es igual a", suma)
# #multiplicación 
# if (len(matrix1[0]) == len(matrix2)):
#     print("Se pueden multiplicar las matrices")
#     # paso2:código de crear una matriz final
#     matrizc= [[0 for _ in range(len(matrix1))] for _ in range(len(matrix2[0]))]
#     print(len(matrix1))
#     print(len(matrix2[0]))

# else:
#     print("No se pueden multiplicar las matrices")
# for i in range(len(matrix1)): #recorrer filas de la matriz A
#     for j in range(len(matrix2[0])): #filas de la matriz B y columna de de la matriz de A
#         # matrizc[i][j]=0
#         for k in range(len(matrix2)): #columnas de la matriz B
#             matrizc[i][j] += matrix1[i][k] * matrix2[k][j]
#         print(matrizc)