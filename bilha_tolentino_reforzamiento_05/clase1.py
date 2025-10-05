"""
1. Crear una clase Empleado que contenga los siguientes métodos, uno que
pida ingresar un nombre, apellido y edad, un método para pedir su sueldo
actual y otro método que lo imprima ambos resultados, pero estarán
contenidos en un diccionario. Comprobar los métodos instanciado la clase
respectivamente al menos para 3 empleados. Considerar en el constructor los
valores necesarios.
"""
class Empleado:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = 0
        self.sueldo = 0.0


    def ingresar_datos(self):
        self.nombre = input("Ingresa el nombre: ")
        self.apellido = input("Ingresa el apellido: ")
        self.edad = int(input("Ingresa la edad: "))


    def ingresar_sueldo(self):
        self.sueldo = float(input("Ingresa el sueldo actual: "))


    def mostrar_datos(self):
        datos = { "nombre": self.nombre, "apellido": self.apellido,"edad": self.edad, "sueldo": self.sueldo}
        print(datos)

print("=== Empleado 1 ===")
empleado1 = Empleado()
empleado1.ingresar_datos()
empleado1.ingresar_sueldo()
empleado1.mostrar_datos()

print("\n=== Empleado 2 ===")
empleado2 = Empleado()
empleado2.ingresar_datos()
empleado2.ingresar_sueldo()
empleado2.mostrar_datos()

print("\n=== Empleado 3 ===")
empleado3 = Empleado()
empleado3.ingresar_datos()
empleado3.ingresar_sueldo()
empleado3.mostrar_datos()