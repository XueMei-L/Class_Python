# Qué es un diccionario?
# Un diccionario es una esctructura de datos que almacena pares clave-valor.

# ¿Cómo se crea un diccionario?
# se cre con {}

# Ejemplo:

empleado = {
    "nombre": "Ana",
    "edad": 25,
    "cuidad": "Tenerife",
}

print(empleado)

# imprimir algún valor concreto
print(empleado["nombre"])
print(empleado["edad"])
print(empleado["cuidad"])
# print(empleado["residencia"]) # KeyError: 'residencia', porque la clave no existe

# imprimir otra forma alternativa
print(empleado.get("nombre"))
print(empleado.get("residencia")) # None, devolve None, es más seguro.

# Modificacion del diccionario
empleado = {
    "nombre": "Ana",
    "edad": 25,
    "cuidad": "Tenerife",
}

# agregar una nueva clave-valor
empleado["genero"] = "Femenino"

print(empleado)

# Actualizar un valor según la clave.
empleado["cuidad"] = "Lanzarote"

print(empleado)

# Eliminar un clave-valor
# 1. usar del
del empleado["cuidad"]

print(empleado)

# 2. usar pop
empleado["cuidad"] = "Lanzarote" #alt + teclado abajo

empleado.pop("cuidad")
print(empleado)


# iteracion sobre un diccionario
empleado = {
    "nombre": "Ana",
    "edad": 25,
    "cuidad": "Tenerife",
    "genero": "Femenino",
    "trabajo": "Ingeniera",
}

# iterar utilizando el bucle for
for clave in empleado:
    print(f"{clave}: {empleado[clave]}") # empleado[nombre] # empleado[edad] # empleado[cuidad] # empleado[genero] # empleado[trabajo]

for valor in empleado.values():
    print(valor)


# Metodos de un diccionario
# ctrl + f2 -> enter -> para salir hace esc
# ctrl + z -> deshacer

empleado = {
    "nombre": "Ana",
    "edad": 25,
    "cuidad": "Tenerife",
    "genero": "Femenino",
    "trabajo": "Ingeniera",
}

# dict.keys()	Devuelve todas las claves
# resivsar las claves existentes
empleado_keys = empleado.keys()
print(empleado_keys)

# dict.values()	Devuelve todos los valores
empleado_values = empleado.values()
print(empleado_values)

# dict.items()	Devuelve pares clave-valor
empleado_items = empleado.items()
print(empleado_items)

# dict.get(clave, default)	Obtiene valor o default


# dict.pop(clave)	Elimina clave y devuelve valor


# dict.popitem()	Elimina último par clave-valor
empleado_popitem = empleado.popitem()
print(empleado_popitem)
print(empleado)

# dict.update(otro_dict)	Añade o actualiza claves con otro diccionario


# dict.clear()	Elimina todos los elementos
empleado_clear = empleado.clear()
print(empleado_clear)



# Direccionarios añadidos
# alt + shift + arriba / abajo - copiar la misma linea del codigo arriba o abajo
# ctrl + x -> cortar la linea del codigo

# alumno = {
#     "nombre": "Ana",
#     "edad": "16",
#     "notas": { 
#         "matematicas": 8,
#         "lengua": 10,
#         "ingles": 6, 
#     },
# }

# print(alumno["notas"]["matematicas"])


# imprimir con varios alumnos
# Fallo: la clave no se puede repetir, porque en este caso, estoy ponendo nombres muchas veces, tengo que separarlo.
# alumnos = {
#     "nombre": "Ana",
#     "edad": 16,
#     "notas": { 
#         "matematicas": 8,
#         "lengua": 10,
#         "ingles": 6, 
#     },

#     "nombre": "Juan",
#     "edad": 16,
#     "notas": { 
#         "matematicas": 5,
#         "lengua": 9,
#         "ingles": 7, 
#     },

#     "nombre": "Pepe",
#     "edad": 16,
#     "notas": { 
#         "matematicas": 7,
#         "lengua": 3,
#         "ingles": 5, 
#     }
# }

# alumnos = {
#     "alumno1": {
#         "nombre": "Ana",
#         "edad": 16,
#         "notas": {"matematicas": 8, "lengua": 10, "ingles": 6}
#     },
#     "alumno2": {
#         "nombre": "Pepe",
#         "edad": 16,
#         "notas": {"matematicas": 5, "lengua": 9, "ingles": 7}
#     },
#     "alumno3": {
#         "nombre": "Juan",
#         "edad": 16,
#         "notas": {"matematicas": 7, "lengua": 3, "ingles": 5}
#     },
#     "alumno4": {
#         "nombre": "Susana",
#         "edad": 16,
#         "notas": {"matematicas": 7, "lengua": 3, "ingles": 5}
#     }
# }

# for clave, datos in alumnos.items():
#     print(f"numeroDeAlumno: {clave}")
#     print(f"Nombre: {datos.get('nombre')}")
#     print(f"Edad: {datos.get('edad')}")
#     print("Notas:")
    
#     # 🔹 Recorremos las notas usando .items() también
#     for materia, nota in datos["notas"].items():
#         print(f"-{materia.capitalize()}: {nota}")
    
#     print("-" * 30)

# Tarea 1:
# Eres ingeniero de una empresa, ahora tienes que crear un sistema para guardar los datos de todos los empleaods de la empresa
# en el sistema tienes que guardar la id (número de identidad - es único) de cada empleado, 
# nombre, edad, genero, departamento, sueldo, y proyectos que está haciendo cada uno.
# por ejemplo:
empleado: {
    id: "X001",
    "nombre": "Juan Antonio",
    "edad": 35,
    "genero": "hombre",
    "departamento": "IT",
    "sueldo": 2000,
    "proyectos":{
        "python": "en el proceso de correcion",
        "calculo": "terminado",
        "pruebaDeTest": "pendiente",
    }
}


# Tarea 1: esto es una lista de listas, puede convertir en un diccionario con los metodos o las funciones que hemos aprendido.
empleados = [
    ["X001", "Juan Antonio", 35, "hombre", "IT", 2000, {"python":"en proceso","calculo":"terminado","pruebaDeTest":"pendiente"}],
    ["X002", "María López", 28, "mujer", "Marketing", 1800, {"campañaVerano":"terminado","redesSociales":"en progreso"}],
    ["X003", "Carlos García", 40, "hombre", "IT", 2500, {"python":"pendiente","seguridadWeb":"en desarrollo"}],
    ["X004", "Ana Torres", 32, "mujer", "Recursos Humanos", 2100, {"entrevistas":"terminado","evaluaciones":"en revisión"}],
    ["X005", "Pedro Sánchez", 45, "hombre", "Compras", 2300, {"proveedores":"terminado","controlStock":"en progreso"}],
    ["X006", "Lucía Fernández", 29, "mujer", "Ventas", 1900, {"objetivosQ1":"terminado","clientesVIP":"pendiente"}],
    ["X007", "David Romero", 37, "hombre", "IT", 2600, {"python":"terminado","inteligenciaArtificial":"en progreso"}],
    ["X008", "Sofía Navarro", 31, "mujer", "Finanzas", 2200, {"presupuestos":"en revisión","gastos2025":"pendiente"}],
    ["X009", "Miguel Herrera", 42, "hombre", "IT", 2700, {"python":"en proceso","servidores":"terminado"}],
    ["X010", "Laura Ruiz", 34, "mujer", "Diseño", 2000, {"branding":"en progreso","nuevaImagen":"terminado"}]
]

# 0. crear 10 empleados en un diccionario y imprimir
# algo así
# empleados = {
#     "X001": {...},
#     "X002": {...},
#     # ...
# }

# Convertir lista en diccionario
employees = {
    "X001": {"name": "Alice", "age": 30, "department": "HR", "position": "Manager"},
    "X002": {"name": "Bob", "age": 28, "department": "IT", "position": "Developer"},
    "X003": {"name": "Charlie", "age": 35, "department": "Sales", "position": "Analyst"}
    # ....
}


empleadosDiccionario = {}
for empleado in empleados:
    empleadosDiccionario[empleado[0]] = {
        "nombre": empleado[1],
        "edad": empleado[2],
        "genero": empleado[3],
        "departamento": empleado[4],
        "sueldo": empleado[5],
        "proyectos": empleado[6]
    }


# Imprimir todos los empleados
# for id, datos in empleadosDiccionario.items():
#     print(id, "=>", datos)

# for empleado in empleadosDiccionario.values():
#     print(empleado)

for id, datos in empleadosDiccionario.items():
    print(id, "=>", datos)


# # 1. filtrar los empleados que son mayor de 35 años
print("\nEmpleados mayores de 35 años:")
for id, datos in empleadosDiccionario.items():
    # id = xx01
    # datos = {'nombre': 'Juan Antonio', 
    #           'edad': 35, 
    #           'genero': 'hombre', 
    #           'departamento': 'IT', 
    #           'sueldo': 2000, 
    #           'proyectos': {'python': 'en proceso', 'calculo': 'terminado', 'pruebaDeTest': 'pendiente'}}
    if datos["edad"] > 35:
        print(datos["nombre"], "-", datos["edad"], "años")

    # if datos["proyectos"]["python"] == "en proceso":
    #     print(datos["nombre"], "-", datos["proyectos"]["python"])

        
# # 2. filtrar los empleados que estan trabajando en el departamento de IT con el proyecto Python.
print("\nEmpleados de IT con proyecto Python:")
for id, datos in empleadosDiccionario.items():
    if datos["departamento"] == "IT" and "python" in datos["proyectos"]:
        print(datos["nombre"], "-", datos["proyectos"]["python"])


# # 3. añadir un empleado nuevo con los siguientes datos
empleadosDiccionario["X011"] = {
    "nombre": "Carmen Díaz",
    "edad": 30,
    "genero": "mujer",
    "departamento": "IT",
    "sueldo": 2400,
    "proyectos": {"python": "pendiente", "appMovil": "en desarrollo"}
}

for id, empleado in empleadosDiccionario.items():
    print(id, "=>", empleado)

# print("\nNuevo empleado añadido:")
# print("X011:", empleadosDiccionario["X011"])

# 4. echar a un empleado a un departamento de it a departamento de compras.
# primera forma
# empleadosDiccionario["X007"]["departamento"] = "Compras"

# # segunda forma
# for id, datos in empleadosDiccionario.items():
#     if datos["departamento"] == "IT":
#         datos["departamento"] = "Compras"
#         print(f"\n{datos['nombre']} ha sido transferido al departamento de Compras.")
#         break  # solo cambia uno


# Subir sueldo de cada empleado
print("\n--------------------------------------------------------------------")
for id, datos in empleadosDiccionario.items():
    datos["sueldo"] += 200
    print(f"Sueldo actualizado de {datos['nombre']}: {datos['sueldo']} €")

print("\nTodos los sueldos han sido incrementados en 200 €.")

for id, empleado in empleadosDiccionario.items():
    print(id, "=>", empleado)


# comandos para subir al github por la segunda vez
# git add .
# git commit -m "xxxxxxxxx"
# git push


