# clase Calculadora
# qué atributo necesitamos: x, y
# qué metodos hay: + - * / modulo potencia

class Calculator:
    def __init__(self):
        self.result = 0     # inicializar resultado = 0
        self.history = []    # una lista para guardar los resultados

    # metodos 
    def add(self, x, y):
        self.result = x + y
        self.history.append(self.result)
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        self.history.append(self.result)
        return self.result
    
    def multiply(self, x, y):
        self.result = x * y
        self.history.append(self.result)
        return self.result

    def divide(self, x, y):
        if y == 0:
            print("no se puede realizar la division con 0")
        else:
            self.result = x / y
            self.history.append(self.result)
            return self.result

    def module(self, x, y):
        if y == 0:
            print("no se puede realizar el modulo con 0")
        else:
            self.result = x // y   # operador modulo
            self.history.append(self.result)
            return self.result
    
    def power(self, x, y):
        self.result = pow(x, y)
        self.history.append(self.result)
        return self.result
    
    def show_history(self):
        return self.history      # mostrar directamente

    def clear_history(self):
        self.history.clear()
        return "ya has eliminado toda la historia"


obj_calulator = Calculator()
print(obj_calulator.add(10, 5))
print(obj_calulator.subtract(50, 25))
print(obj_calulator.multiply(6, 7))
print(obj_calulator.divide(42, 2))
print(obj_calulator.module(5, 2))         # 2
print(obj_calulator.power(4, 3))          # 64
print(obj_calulator.show_history())
print(obj_calulator.clear_history())