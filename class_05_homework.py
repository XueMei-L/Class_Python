# Vas a programar un sistema que guarda la información de todas las plantas de un edificio, 
# incluyendo los residentes, su edad, género y la cuota de comunidad que pagan.

edificio = {
    "planta0": {
        "numero_personas": 2,
        "personas": [
            {"nombre": "Ana", "edad": 30, "genero": "F"},
            {"nombre": "Luis", "edad": 35, "genero": "M"}
        ],
        "comision_comunidad": 50
    },
    "planta1": {
        "numero_personas": 3,
        "personas": [
            {"nombre": "María", "edad": 28, "genero": "F"},
            {"nombre": "Pedro", "edad": 40, "genero": "M"},
            {"nombre": "Lucía", "edad": 20, "genero": "F"}
        ],
        "comision_comunidad": 70
    },
    "planta2": {
        "numero_personas": 1,
        "personas": [
            {"nombre": "Roberto", "edad": 50, "genero": "M"}
        ],
        "comision_comunidad": 40
    }
}

# Tareas que debe realizar el programa

# 0. Imprimir toda la información del edificio. (Nombre, edad, género y comisión de cada planta.)
# nombre de la planta = "planta3"
# numero_personas = 2
# personas = [
#     {"nombre": "Marta", "edad": 50, "genero": "mujer"},
#     {"nombre": "Andrés", "edad": 55, "genero": "hombre"}
# ]
# comision_comunidad = 60.0

# "planta3": {
#     "numero_personas": 2,
#     "personas": [
#         {"nombre": "Marta", "edad": 50, "genero": "mujer"},
#         {"nombre": "Andrés", "edad": 55, "genero": "hombre"}
#     ],
#     "comision_comunidad": 60.0
# }

# usa algo edificio[clave] = valor


# 2. Calcular el total de la comisión de comunidad del edificio.

# 3. Contar cuántas personas viven en total.

# 4. Filtrar y mostrar solo las personas mayores de 30 años.

# 5. Agregar una nueva persona a una planta.

# 6. Eliminar una persona de una planta (por nombre).

# 7. Cambiar la comisión de comunidad de una planta.