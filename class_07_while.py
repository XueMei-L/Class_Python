# while condicion:
    # codigo


# Ejercicio 1: imprimir el resultado de 1-100 utilizando el while
print("-----------------------Ejercicio1-----------------------")
i = 1
suma = 0

while i <= 100:
    # realizar la suma de valores
    suma += i
    # incrementando el valor para salir del while
    i += 1

print(suma)


print("-----------------------Ejercicio2-----------------------")

password_correct = "123456"

password = ""

# Ejercicio 2: Comprobar una contraseña indicada
while password != password_correct:
    password = input("Introduzca la contraseña:")
    if(password != password_correct):
        print("Contraña incorrecta, vuelva a intentarlo")

print("Contraseña correcta")



print("-----------------------Ejercicio3-----------------------")
# Tarea 1: ¿Qué pasaría si ejecuto los siguientes códigos?
while True:
    print("hello world")

# Tarea 2: Factorial con while
# por ejemplo factorial de es : 5! = 5*4*3*2*1 = 120
numero = int(input("Introduce un número para calcular su factorial: "))

resultado = 1  
i = 1           

while i <= numero:
    resultado *= i  # 1 * 1 * 2 * 3    5*4*3*2*1
    i += 1          # 2  

print("El factorial es:", resultado)
a = 0
b = 1


numero = int(input("Introduce un número para calcular su factorial: "))

factorial = 1
contador = numero

while contador > 1:
    factorial *= contador
    contador -= 1

print(f"El factorial de {numero} es: {factorial}")

# -------------------------------------------------------------------------------------

# Tarea 3: Imprimir la Serie de Fibonacci hasta 100 / busca el concepto en google si no entiendes
# F(0) = 0  # la primera vez es 0, por que el primer valor es 0
# F(1) = 1  # la segunda vez es 1, por que el segundo valor es 1
# F(2) = 1  # la tercera vez es 1, por que el tercer valor es 0 + 1 = 1
# F(n) = F(n-1) + F(n-2)

a = 0
b = 1

while a <= 100:
    print(a)
    c = a + b
    a = b
    b = c


# Tarea 4: Buscar divisores de un número indicado por el usuario usando while

num = int(input("Introduce un número: "))
i = 1

print("Divisores:")

while i <= num:
    if num % i == 0:
        print(i)
    i += 1
