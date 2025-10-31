# create a tuple
my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)

print(my_tuple[0])

# create a tuple with different data
mixed_tuple = (10, "hello", 9.99, True)
print(mixed_tuple)

tuple1 = (1,)

# tuple auto
tuple2 = 1, 2, 3
print(type(tuple2))

# error of tuple, can not modify
# my_tuple[0] = 10
# print(my_tuple[0])

print(my_tuple[1:3]) 

# methods of tuple
tuple3 = 1, 2, 3, 4, 2, 2

# count()
print(tuple3.count(2))

# index()
print(tuple3.index(3))


# desempaquetado de tuplas
tuple_person = ("Lilia", 1999, "China")
name, year, country = tuple_person

print("My name is", name, "I born in", year, "in", country, ".")

# the use of tuple
color_rgb = (255, 0, 0) # red color

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#convert my tuple to list
list_color_rgb = list(color_rgb)

#------------------------------------------------------------------------------------------------------------------------

# Excercise 01:
# Tienes una tupla que contiene informacion de varios estudiantes:
estudiantes = (
    ("Ana", (8, 9, 10)),
    ("Luis", (7, 6, 9)),
    ("Maria", (10, 10, 9))
)
# 1. Calcular el promedio de cada estudiante e imprimir su nombre junto con su promedio(con dos decimales).
for estudiante in estudiantes:
    nombre, notas = estudiante
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")
# 2. Encontrar estudiante que tiene mejor nota en tercer cuatrimestre e imprimir su nombre.
mejor_nota = -1
mejor_estudiante = ""
for estudiante in estudiantes:
    nombre, notas = estudiante
    if notas[2] > mejor_nota:
        mejor_nota = notas[2]
        mejor_estudiante = nombre
print(f"El estudiante con mejor nota en el tercer cuatrimestre es: {mejor_estudiante} con una nota de {mejor_nota}")

#------------------------------------------------------------------------------------------------------------------------

# forma alternativa:
# 1. Nombre y promedio
for nombre, notas in estudiantes:
    promedio = sum(notas)/len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")
    
# 2. Estudiante con la nota más alta en el último examen
ultimo_examen = [notas[-1] for _, notas in estudiantes] 

# _ → toma el primer elemento (el nombre del estudiante), pero no lo usamos.
# notas → toma la segunda parte (la tupla de notas).

max_nota = max(ultimo_examen)
indice = ultimo_examen.index(max_nota)
print(f"Estudiante con la nota más alta en el último examen: {estudiantes[indice][0]}")

#------------------------------------------------------------------------------------------------------------------------

# Excercise 02:
# Desempaquetar la tupla y imprimir la informacion de cada valor: Madrid = 
datos = ("Madrid", 2025, (28.3, -16.6))
city, year, (max_temp, min_temp) = datos
print("La cuidad =", city, "", year, ",", max_temp, ",", min_temp)
# con 3 lineas de codigo

#------------------------------------------------------------------------------------------------------------------------


from datetime import datetime

# Excercise 03:
# Crear un sistema que guarde los datos de 10 empleados usando una tupla de tuplas, y luego filtrar los empleados mayores de 30 años.
empleados = (
    ("Ana", "15/03/1992", "Mujer"),
    ("Luis", "22/07/1985", "Hombre"),
    ("Carmen", "09/10/2001", "Mujer"),
    ("Pablo", "03/12/1990", "Hombre"),
    ("Sofía", "28/04/1998", "Mujer"),
    ("Miguel", "12/06/1980", "Hombre"),
    ("Laura", "19/11/1993", "Mujer"),
    ("Javier", "25/01/2002", "Hombre"),
    ("Elena", "07/09/1988", "Mujer"),
    ("Diego", "30/05/1995", "Hombre")
)
today = datetime.now()

for empleados in empleados:
    name, birth_date, gender = empleados
    day, month, year = map(int, birth_date.split('/'))
    age =  today.year - year
    if age > 30:
        print(f"Nombre: {name}, Edad: {age}, Género: {gender}")
    
#------------------------------------------------------------------------------------------------------------------------