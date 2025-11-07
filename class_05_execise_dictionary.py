# Dado un diccionario, crea uno nuevo en el que las claves y valores estén intercambiados.

# Ejemplo:
original = {
    "nombre": "Lilia",
    "edad": 25,
    "ciudad": "Tenerife"
}

# Resultado esperado:
# {
#     "Lilia": "nombre",
#     25: "edad",
#     "Tenerife": "ciudad"
# }

invers = {}
for clave, valor in original.items():
    invers[valor] = clave

#-----------------------------------------------------------------------

# numeros = [2, 3, 4, 2, 3, 2, 5, 3]

# resultado esperado:
# {
#     2: 3,
#     3: 3,
#     4: 1,
#     5: 1
# }
numeros = [2, 3, 4, 2, 3, 2, 5, 3]

frecuencia = {}

for num in numeros:
    frecuencia[num] = frecuencia.get(num, 0) + 1

print(frecuencia)

for numero, cuenta in frecuencia.items():
    print(f"El número {numero} aparece {cuenta} veces.")

#-----------------------------------------------------------------------

alumnos = {
    "Juan": {"matematicas": 8, "ingles": 9, "historia": 7},
    "Maria": {"matematicas": 7, "ingles": 10, "historia": 9},
    "Carlos": {"matematicas": 6, "ingles": 8, "historia": 6},
    "Ana": {"matematicas": 9, "ingles": 9, "historia": 10},
    "Lucia": {"matematicas": 5, "ingles": 6, "historia": 7},
    "Pedro": {"matematicas": 8, "ingles": 7, "historia": 8},
    "Sofia": {"matematicas": 10, "ingles": 10, "historia": 9},
    "Miguel": {"matematicas": 7, "ingles": 6, "historia": 7},
    "Laura": {"matematicas": 8, "ingles": 9, "historia": 10},
    "David": {"matematicas": 6, "ingles": 8, "historia": 7}
}

# calcular el promedio de cada alumno y mostrar en un diccionario su nombre y su promedio
alumnos_promedio = {}

for nombre_alumno, notas in alumnos.items():
    promedio = sum(notas.values()) / len(notas)
    # (8 + 9 + 7) / 3
    print(f"El promedio de {nombre_alumno} es {promedio:.2f}")
    alumnos_promedio[nombre_alumno] = promedio

for nombre_alumno, promedio in alumnos_promedio.items():
    print(f"{nombre_alumno}: {promedio:.2f}")

