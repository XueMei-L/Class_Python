# numbers = [1, 2, 3, 4, 5]
# # 0 1 2 3 4

# print(numbers)

# # # recorrer la lista por elementos
# # for number in numbers:
# #     print(number)

# # # recorrer la lista por índices
# # for i in range(len(numbers)):
# #     print(numbers[i])

# frutas = ["manzana", "banana", "naranja", "kiwi"]
# print(frutas[0])    
# print(frutas[-1])   
# print(frutas[1:3])  
# print(frutas[:2])   
# print(frutas[2:])   
# print(frutas[::-1])  # lista invertida


# numbers = [1, 2, 3, 4, 5]
# # quiero numeros pares 


# Metodos de lista
numbers = [3, 1, 4]

# // añadir un número 2 al final de la lista
numbers.append(2)
print(numbers) 

# // insetar un número 10 en la 1er posición  de la lista.
numbers.insert(1, 10)
print(numbers)

# // agregar número 2 y 5 a la vez al final de la lista.
# numbers.append([2,5])
numbers.extend([2,5])
print(numbers)

# // eliminar número 3 en la lista.
numbers.remove(3)
print(numbers)

# // eliminar el número que está en la ultima posición y devulver el número eliminado.
elimited = numbers.pop()
print(elimited)
print(numbers)

# // devuelve la posición del número 10
index = numbers.index(10)
print(index)
print(numbers)

# // añadir otra vez un número 2 al final de lista.
numbers.append(2)
print(numbers)

# // contar cuantas veces aparece el número 2
count = numbers.count(2)
print(count)

# // ordenar la ista 
numbers.sort()
print(numbers)

frutas = ["manzana", "banana", "naranja", "kiwi"]
frutas.sort()
# a - z

values = [True, False, True, False]
values.sort()
print(values)

# // invertir el orden de la lista
numbers.reverse()
print(numbers)

# comentar varias lineas
# ctrl + k 
# ctrl + c 

# descomentar varias lineas
# ctrl + k
# ctrl + u
# **Tarea para casa:**

# 1. Crea una función `palabras_unicas(s)` que recibe la cadena “**electroencefalografista”**  y meter en una lista y devuelva una lista ordenada de palabras sin repetir, imprimir resultado de cada paso**.
    
#     ```python
#     def palabras_unicas(s):
#         // códigos
#         return // cídogos
#     ```
    
# 2. Escribe un programa que reciba una lista de números y devuelva todas las parejas cuya suma sea par.