# Tareas que debe realizar el programa

# 0. Imprimir toda la información del edificio. (Nombre, edad, género y comisión de cada planta.)

# 1. Agregar una nueva planta al edificio con su información correspondiente.

# usa algo edificio[clave] = valor

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


# 2. Calcular el total de la comisión de comunidad del edificio.

# 3. Contar cuántas personas viven en total.

# 4. Filtrar y mostrar solo las personas mayores de 30 años.

# 5. Agregar una nueva persona a una planta.

# 6. Eliminar una persona de una planta (por nombre).

# 7. Cambiar la comisión de comunidad de una planta.


edificio = {
    "planta1": {
        "numero_personas": 2,
        "personas": [
            {"nombre": "Ana", "edad": 25, "genero": "mujer"},
            {"nombre": "Luis", "edad": 30, "genero": "hombre"}
        ],
        "comision_comunidad": 50.0
    },
    "planta2": {
        "numero_personas": 3,
        "personas": [
            {"nombre": "Carlos", "edad": 40, "genero": "hombre"},
            {"nombre": "Lucía", "edad": 35, "genero": "mujer"},
            {"nombre": "Pepe", "edad": 20, "genero": "hombre"}
        ],
        "comision_comunidad": 70.0
    }
}

# show information of the building.
def mostrar_informacion(edificio):
    for planta, datos in edificio.items():
        print(f"\n{planta.upper()}:")
        print(f"  Número de personas: {datos['numero_personas']}")
        print(f"  Comisión comunidad: {datos['comision_comunidad']}")
        print("  Personas:")
        for p in datos["personas"]:
            print(f"    - {p['nombre']}, {p['edad']} años, {p['genero']}")

# add a new floor to the building
def agregar_planta(edificio, nombre_planta, numero_personas, personas, comision):
    edificio[nombre_planta] = {
        "numero_personas": numero_personas,
        "personas": personas,
        "comision_comunidad": comision
    }

# calculate total community commission
def total_comision(edificio):
    total = sum(p["comision_comunidad"] for p in edificio.values())
    return total

# filter of people older than 30
def mayores_30(edificio):
    mayores = []
    for planta in edificio.values():
        for persona in planta["personas"]:
            if persona["edad"] > 30:
                mayores.append(persona)
    return mayores

def agregar_persona(edificio, planta, persona):
    edificio[planta]["personas"].append(persona)
    edificio[planta]["numero_personas"] += 1

# review
def eliminar_persona(edificio, planta, nombre):
    personas = edificio[planta]["personas"]
    edificio[planta]["personas"] = [p for p in personas if p["nombre"] != nombre]
    edificio[planta]["numero_personas"] = len(edificio[planta]["personas"])

# change community commission of a floor
def cambiar_comision(edificio, planta, nueva_comision):
    edificio[planta]["comision_comunidad"] = nueva_comision


# hacer un switch para ejecutar las tareas
# ----------------------Bienvenido al sistema de gestion del edificio----------------------
# Elija la opción que desea realizar:
# 1. Mostrar la información del edificio
# 2. Agregar una nueva planta
# 3. Agregar una nueva persona a una planta
# 4. Calcular el total de la comisión de comunidad
# 5. Eliminar una perona de una planta
# 6. Cambiar la comisión de comunidad de una planta


def main():

    # 1. Mostrar la informacion usando la funcion
    mostrar_informacion(edificio)

    # 2. Agregar una nueva planta al edificio con su información correspondiente.
    agregar_planta(edificio, "planta3",2, [{"nombre": "Marta", "edad": 50, "genero": "mujer"},
    {"nombre": "Andrés", "edad": 55, "genero": "hombre"}], 60.0)

    # 3. Mostrar la informacion usando la funcion
    mostrar_informacion(edificio)

    # 4. Mostrar el total de la comisión de comunidad del edificio.
    total =total_comision(edificio)
    print(f"\nTotal comisión de comunidad del edificio: {total}")

    # 5. Mostrar las personas mayores de 30 años.
    # personas_mayores es una lista
    personas_mayores = mayores_30(edificio)
    for persona in personas_mayores:
        print(f" - {persona['nombre']}, {persona['edad']} años, {persona['genero']}")
    
    # 6. agregar una nueva persona
    # {"nombre": "Sofía", "edad": 28, "genero": "mujer"}
    agregar_persona(edificio, "planta3", {"nombre": "Sofía", "edad": 28, "genero": "mujer"})

    # 7. Mostrar la informacion usando la funcion
    mostrar_informacion(edificio)

    # 8. eliminar una personas
    eliminar_persona(edificio, "planta3", "Ana")

    mostrar_informacion(edificio)

    cambiar_comision(edificio, "planta3", 80.0)

    mostrar_informacion(edificio)

# forma de ejecutar el script
if __name__ == "__main__":
    main()