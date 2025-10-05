"""
4. Crear una clase Alumno que tenga como atributos el nombre, edad y la
nota final del alumno. Crear los métodos para inicializar sus atributos, otro
para imprimirlos y un método para mostrar un mensaje con el resultado de la
nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar la clase
por lo menos 4 veces (4 alumnos)
"""
class alumno:

    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final


    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota final: {self.nota_final}")


    def verificar_aprobacion(self):
        if self.nota_final >= 13:
            print(f" {self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} no ha aprobado.")


alumno1 = alumno("Ana", 19, 15)
alumno2 = alumno("Carlos", 20, 10)
alumno3 = alumno("Lucía", 18, 17)
alumno4 = alumno("Jorge", 22, 12)


for alumno in [alumno1, alumno2, alumno3, alumno4]:
    print("\n--- Datos del alumno ---")
    alumno.mostrar_datos()
    alumno.verificar_aprobacion()
