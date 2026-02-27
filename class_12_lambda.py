# Lambda

# ¿Qué es lambda en python?
# lambda es una funcion anonima

# lambda argumentos : expresion
# lambda a : a + a
# x = lambda a, b, c : a + b - c

# Cuando se usa lambda
# 1. Cuando mi funcion es muy simple o que se puede escribir en una linea
# 2. Para cuando hay una funcion de prueba
# 3. Cuando usamos tipo map, filter, sorted estos metodos, utilizamos lambda para programar

# def main():
#     # x = lambda a : a + 2
#     # print(x(5))

#     # y = lambda a, b: a*b
#     # print(y(1, 2))

#     # con metodo sorted
#     # students = ["Alice", "Bob", "Charlie", "David"]
#     # sorted_students = sorted(students, key=lambda x: len(x))
#     # print(sorted_students)

#     # con metodo map
#     # numbers = [1, 2, 3, 4, 5]
#     # squared = list(map(lambda x: x**2, numbers))
#     # print(squared)

#     # con metodo filter
#     # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     # evens = list(filter(lambda x: x % 2 == 0, numbers))
#     # print(evens)

#     # doble lambda
#     # multiply_by = lambda n: lambda x : x * n

#     # def multyply_by(n):
#     #     def multiply_by(x):
#     #         return x * n

#     pass
    



# if __name__ == "__main__":
#     main()



# Tarea:
# 1. Escribir 3 lambda con 3 metodos con diferentes condiciones:
    # 1.1 dada una lista, nums = [15, 22, 9, 30, 17, 6, 25], escribe la lambda con metodo filter
    #    para filtrar numero sea divisible por 3 y 5

    # 1.2 dos listas, a = [1, 2, 3, 4] 和 b = [10, 20, 30, 40], utiliza la lambda con metodo map 
    # para calcular la multiplicacion de misma posicion
    # por ejemplo: 1 * 10 = 19， 2 * 20 = 40, la salida es [10, 40, 90, 160]


# 2. Escriba un programa que calcule la media de cuatros valores introducidos por el usuario:
# primer valor: 10
# segundo valor: 20
# tercer valor: 30
# cuarto valor: 40
# La media es: 25


a = [10, 20, 30, 40]
b = 10
c = "hola"
d = True #booleano

def media(param1):
    param1 = [10,20,30,40]
    param1[0] # 10
    param1[1] # 20
    param1[2] # 30
    param1[3] # 40

    print(param1)

media(a)