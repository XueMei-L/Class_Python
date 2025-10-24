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


# # Metodos de lista
# numbers = [3, 1, 4]

# # // añadir un número 2 al final de la lista
# numbers.append(2)
# print(numbers) 

# # // insetar un número 10 en la 1er posición  de la lista.
# numbers.insert(1, 10)
# print(numbers)

# # // agregar número 2 y 5 a la vez al final de la lista.
# # numbers.append([2,5])
# numbers.extend([2,5])
# print(numbers)

# # // eliminar número 3 en la lista.
# numbers.remove(3)
# print(numbers)

# # // eliminar el número que está en la ultima posición y devulver el número eliminado.
# elimited = numbers.pop()
# print(elimited)
# print(numbers)

# # // devuelve la posición del número 10
# index = numbers.index(10)
# print(index)
# print(numbers)

# # // añadir otra vez un número 2 al final de lista.
# numbers.append(2)
# print(numbers)

# # // contar cuantas veces aparece el número 2
# count = numbers.count(2)
# print(count)

# # // ordenar la ista 
# numbers.sort()
# print(numbers)

# frutas = ["manzana", "banana", "naranja", "kiwi"]
# frutas.sort()
# # a - z

# values = [True, False, True, False]
# values.sort()
# print(values)

# # // invertir el orden de la lista
# numbers.reverse()
# print(numbers)

# comentar varias lineas
# ctrl + k 
# ctrl + c 

# descomentar varias lineas
# ctrl + k
# ctrl + u
# **Tarea para casa:**

# Ejercicio 1:
# 1. pedir al usuario la cadena, la cadena es "electroencefalografistaelectroencefalografiaelectroencefalograma"
cadena = input("Please enter the string: ")

# 2. meter en una lista las letras de la cadena
my_list = list(cadena)
print(my_list)

# 3. hacer que la lista no repita letras
list_unique = list(set(my_list))
print(list_unique)

# 4. ordenar la lista por a-z
list_unique.sort()
print(list_unique)

# 5. imprimir la lista inversa
list_unique.reverse()
print(list_unique)

# 6. imprimir las letras que están en la posicion impar de la lista ordenada
my_list = []  # lista vacía
for i in range(len(list_unique)):
    if i % 2 != 0:
        my_list.append(list_unique[i])
print(my_list)


my_list = [list_unique[i] for i in range(len(list_unique)) if i % 2 != 0]
print(my_list)

# 7. sustituir las letras en las posiciones pares por '*' 
for i in range(len(list_unique)):
    if i % 2 == 0:
        list_unique[i] = '*'

print(list_unique)

# 8. eliminar las dos ultimas letras de la lista y ordenar la lista de nuevo
list_unique.pop()
list_unique.pop()

list_unique.sort()

# 9. mostrar el resultado
print("Result:\n", list_unique)

# Ejercicio 2:
# 1. crear una lista de numeros primos del 1 al 100
# 2. realizar la suma de todos los numeros primos
# 3. mostrar el numero primo más grande y más pequeño
# 4. sumatorio de los numeros primos que son menores de 50

# 1. Create a list of prime numbers from 1 to 100
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# 2. Calculate the sum of all prime numbers
print("Total sum of prime numbers:", sum(prime_numbers))

# 3. Find the largest and smallest prime numbers
print("Largest prime number:", max(prime_numbers))
print("Smallest prime number:", min(prime_numbers))

# 4. Calculate the sum of prime numbers smaller than 50
sum_under_50 = sum([n for n in prime_numbers if n < 50])
print("Sum of prime numbers under 50:", sum_under_50)