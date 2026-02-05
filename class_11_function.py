# para que sirve una funcion?
# funcion sirve para retulizar los codigos

# a = 10
# b = 5

# print(a + b)

# c = 1
# d = 2

# print(c + d)

# e = -1
# f = -5

# print(e + f)


# ----------------------------------------------------------
# definir variables
a = 10
b = 5

# implementacion de la funcion suma

# def = definicion
# suma = nombre de la funcion
# valor1 = primer parametro
# valor2 = segundo parametro
def suma(valor1, valor2):
    print(valor1 + valor2)


# llamada de la funcion suma
suma(a, b)
suma(4, 10)

# ----------------------------------------------------------
# implementacion de la funcion helloworld
def say_hello():
    print("hello world")

say_hello()

# ----------------------------------------------------------
# la diferencia entre print vs return

def suma2(valor1, valor2):
    return valor1 + valor2

resultado = suma2(10, 10) * 2

print(resultado)

# ----------------------------------------------------------
# cualquier cosa que está después de return no hace nada
def test():
    return 10
    print("hello world")
    suma(1, 2)

# ----------------------------------------------------------
# hacer la potencia 2 de un numero, parametro es valor1
def square(valor1):
    return valor1 * valor1
    
print(square(5))

# ----------------------------------------------------------
# Escriba un programa que solicite al usuario el año de su nacimiento y el año actual, y muestre por pantalla la edad del usuario:

# Año de nacimiento: 2000
# Año actual: 2024
# Su edad es 24 años.

# Año de nacimiento: 1986
# Año actual: 2024
# Su edad es 38 años.


# yearOfBorn = int(input("Introduzca tu año de nacimiento: "))
# actualYear = int(input("el año actual es: "))

# def calcuteAge(yearOfBorn, actualYear):
#     age = actualYear - yearOfBorn
#     print("Año de nacimiento:", yearOfBorn)
#     print("Año actual:", actualYear)
#     print("Su edad es", age ,"años")

# calcuteAge(yearOfBorn, actualYear)

# ----------------------------------------------------------
# variable global y local

fullName = "Perez"

# sin parametro
def hello():
    print("hello world")

# con parametro/s
def hello1(name1, name2):
    # una variable local
    nameF = name1 + name2   # Juan Antonio

    # # una variable local usando una variable global
    nameF2 = name1 + name2

    # modificar nameF
    nameF = "Maria"  # Maria

    # para modificar hay que !! indica que es una variable global
    global fullName
    fullName = "123"

    # modifcar variable global
    # fullName = "Maria Perez"
    
    print("hello", nameF)
    print("hello", fullName)


hello()
hello1("Juan", "Antonio")

# ----------------------------------------------------------
# parametro por defecto de una funcion

def function1(country = "Spain"):
    print("Soy de " + country)


function1("China")
function1()



# Error de sintaxis
# def function2(name = "Anonimo", country): # error
#     print(name, country)

# function2(,"China") # da error


def function2(country, name = "Anonimo", sex="women"): # error
    print(name, sex, country)


function2("Spain")
function2("EEUU", "Jenni")
function2("Austria", "Juan", "Man")

# ----------------------------------------------------------
# parametro de tipo lista (cadena, numero, lista, diccionario)

def function3(food):
    for x in food:
        print(x)

function3(["meat", "vegetable", "fruits"])

# ----------------------------------------------------------
# key = value para asignar datos a cada parametro

def function4(child3, child2, child1):
    print(child1)
    print(child2)
    print(child3) 


child1 = "child1"
child2 = "child2"
child3 = "child3"

function4(child1, child2, child3)
function4(child2="Pepe", child1="Fernando", child3="Ana")

# ----------------------------------------------------------
# cualquier parametro / cantidad de pamaratro
# def function5(param1, param2, param3, param4, param5, param6, param7, param8):

def function5(*params):
    print(params[0])
    print(params[1])
    print(params[2])


function5("Pepe", "Ana", "Maria", "Juan", "Fernando", "Jose")

# ----------------------------------------------------------
# cuando una funcion no hay codigos
def function6():
    pass  # sirve para cuando no hay ningun codigo dentro de la funcion








# def main():


# # forma de ejecutar el script
# if __name__ == "__main__":
#     main()
