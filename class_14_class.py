# 14. Class
# 1. Dentro de una clase hay varios atributos y metodos.


# # ---------------------------------------------------------------
# # Cómo se define una class

# # class NombreDeLaClase:
#     # atributos
#     # metodos

# # Ejemplo: 
# # Creacion de una clase en python
# class MyClass:
#     # crear un atributo en la clase
#     x = 5

# # la llamada de la class
# # crear un objeto de la clase MyClass, y luego utilizar "cosas" de la clase
# obj = MyClass()
# print(obj.x)

# # ---------------------------------------------------------------

# # El uso de __init__()
# # Ejemplo: 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Acabas de crear un objeto persona: {self.name}, con edad de {self.age}")

# # p1 = Person("Juan", 18)
# # p2 = Person("Ana", 20)

# # print(p1.name)
# # print(p2.age)

# # falla porque falta argumento de la clase
# # p3 = Person("Julian")

# # ---------------------------------------------------------------
# clase de estudiante
# class Student:
#     def __init__(self, name="Nameless", age="-", claseStudent="X"):
#         self.name = name
#         self.age = age
#         self.claseStudent = claseStudent
#         print(f"Create a new student with name: {self.name}, con age {self.age}, in class {claseStudent}")

# # crear un objeto sin parametros
# student1 = Student()
# print(student1.name)
# print(student1.age)
# print(student1.claseStudent)

# # crear un objeto con parametros
# student2 = Student("Lilia", 26, "A")
# print(student2.name)
# print(student2.age)
# print(student2.claseStudent)

# # ---------------------------------------------------------------

# Crear una clase con metodos
class Cat:
    # atributos = valor / datos
    def __init__(self, name, age, energia):
        self.name = name
        self.age = age
        self.energia = 100
    
    # metodos = accion que realiza
    def ladrar(self):
        return f"{self.name} dice: ¡Miao Miao~!"

    def correr(self, energia):
        # cuando correr cada 3 s, energia -10
        # cuando energia =< 0
        pass

obj_cat = Cat("Ryke", 5)
print(obj_cat.ladrar())
