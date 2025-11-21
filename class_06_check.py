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

# contrl + , 
# hacer un switch para ejecutar las tareas
# ------------------------------Bienvenido al sistema gestion del edificio------------------------------    
# Elija la opción que desea realizar:
#1. Mostrar información del edificio
#2. Agregar planta
#3. Agregar persona a una planta
#4. calcular total comisión de la comunidad
#5. eliminar persona de una planta
# 6. Cambiar la comisión de comunidad de una planta


# xxxxxxx@gmail.com
# 1234567 - formato está mal.
# google limita el formato de respuesta.



def mostrar_informacion():
    print("\n--- Información del edificio ---")
    for planta, datos in edificio.items():
        print(f"{planta}:")
        print(f"  Personas: {datos['numero_personas']}")
        print(f"  Comisión comunidad: {datos['comision_comunidad']}€")
        print("  Lista de personas:")
        for p in datos["personas"]:
            print(f"    - {p['nombre']} ({p['edad']} años, {p['genero']})")
    print("--------------------------------\n")


def agregar_planta():
    nueva = input("Nombre de la nueva planta (ej: planta3): ")
    if nueva in edificio:
        print("Esa planta ya existe.")
        return
    
    edificio[nueva] = {
        "numero_personas": 0,
        "personas": [],
        "comision_comunidad": 0.0
    }
    print(f"Planta '{nueva}' añadida correctamente.")


def agregar_persona():
    planta = input("Ingrese la planta donde añadir la persona: ")

    if planta not in edificio:
        print("Esa planta no existe.")
        return

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    # 1. La edad de la persona agregada no puede ser mayor que 120 años 
    # comprueba la edad que sea menor que 120
    while edad > 120:
        print("La edad no puede ser mayor que 120, introduzca otra edad")
        edad = int(input("Edad: "))
    genero = input("Género(Hombre/Mujer): ")


    edificio[planta]["personas"].append(
        {"nombre": nombre, "edad": edad, "genero": genero}
    )
    edificio[planta]["numero_personas"] += 1

    print(f"Persona '{nombre}' añadida a {planta}.")


def calcular_comision_total():
    total = sum(planta["comision_comunidad"] for planta in edificio.values())
    print(f"\nLa comisión total de la comunidad es: {total}€\n")


def eliminar_persona():
    planta = input("Ingrese la planta: ")
    if planta not in edificio:
        print("Esa planta no existe.")
        return

    nombre = input("Nombre de la persona a eliminar: ")

    personas = edificio[planta]["personas"]
    for p in personas:
        if p["nombre"].lower() == nombre.lower():
            personas.remove(p)
            edificio[planta]["numero_personas"] -= 1
            print(f"Persona '{nombre}' eliminada de {planta}.")
            return

    print("Esa persona no existe en esa planta.")


def cambiar_comision():
    planta = input("Ingrese la planta: ")
    if planta not in edificio:
        print("Esa planta no existe.")
        return

    nueva = float(input("Nueva comisión de comunidad: "))
    edificio[planta]["comision_comunidad"] = nueva

    print(f"Comisión de {planta} actualizada a {nueva}€.")

def main():
    while True:
        print("-----------Bienvenido al sistema de gestion del edificio------------")
        print("1. Mostrar informacion del edificio")
        print("2. Agregar una nueva planta")
        print("3. Agregar una nueva persona a una planta")
        print("4. Calcular el total de la comisión de comunidad")
        print("5. Eliminar una persona de una planta")
        print("6. Cambiar la comision de cominudad de una planta")
        print("0. Salir del programa")

        option = int(input("\nSeleccione una opción:"))

        print(option)

        match option:
            case 1:
                mostrar_informacion()
            case 2:
                agregar_planta()
            case 3:
                agregar_persona()
            case 4:
                calcular_comision_total()
            case 5:
                eliminar_persona()
            case 6:
                cambiar_comision()
            case 0:
                print("Salir del sistema.....")
                break
            case _:
                print("Opción invalida, elige otra opción")
                




# forma de ejecutar el script
if __name__ == "__main__":
    main()