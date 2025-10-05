"""
5. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un método para mostrar los datos e indicar si la persona es
mayor de edad o no y otro método que bonificación que retornará el 20%
adicional de su sueldo, en caso sea mayor de edad. Un método para saber
cuántos meses ha estado trabajando en la empresa

Instanciar por lo menos la clase con 3 diferentes personas.
"""
class Persona:
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.meses_trabajados = meses_trabajados

    def mostrar_datos(self):
        print("\nNombre:", self.nombre)
        print("Edad:", self.edad, "años")
        print("Sueldo: S/.", self.sueldo)
        print("Meses trabajados:", self.meses_trabajados)

        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

    def bonificacion(self):
        if self.edad >= 18:
            bono = self.sueldo * 0.20
            print("Bonificación (20%): S/.", bono)
        else:
            print("No recibe bonificación por ser menor de edad.")

    def mostrar_meses_trabajados(self):
        print(self.nombre, "ha trabajado", self.meses_trabajados, "meses en la empresa.")



persona1 = Persona("Bilha", 21, 1500, 10)
persona2 = Persona("Carlos", 17, 800, 4)
persona3 = Persona("María", 30, 2500, 24)


persona1.mostrar_datos()
persona1.bonificacion()
persona1.mostrar_meses_trabajados()

persona2.mostrar_datos()
persona2.bonificacion()
persona2.mostrar_meses_trabajados()

persona3.mostrar_datos()
persona3.bonificacion()
persona3.mostrar_meses_trabajados()