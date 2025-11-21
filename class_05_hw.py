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
def mostrar_informacion(edificio):
    for planta, datos in edificio.items():
        print(f"\n{planta.upper()}:")
        print(f"  Número de personas: {datos['numero_personas']}")
        print(f"  Comisión comunidad: {datos['comision_comunidad']}")
        print("  Personas:")
        for p in datos["personas"]:
            print(f"    - {p['nombre']}, {p['edad']} años, {p['genero']}")

def agregar_planta(edificio, nombre_planta, numero_personas, personas, comision):
    edificio[nombre_planta] = {
        "numero_personas": numero_personas,
        "personas": personas,
        "comision_comunidad": comision
    }

def total_comision(edificio):
    total = sum(p["comision_comunidad"] for p in edificio.values())
    return total

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

def eliminar_persona(edificio, planta, nombre):
    personas = edificio[planta]["personas"]
    edificio[planta]["personas"] = [p for p in personas if p["nombre"] != nombre]
    edificio[planta]["numero_personas"] = len(edificio[planta]["personas"])

def cambiar_comision(edificio, planta, nueva_comision):
    edificio[planta]["comision_comunidad"] = nueva_comision
    
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

