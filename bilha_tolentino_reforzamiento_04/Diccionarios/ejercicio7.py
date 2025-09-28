"""
Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y
las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""

cantidad = int(input("Cantidad de alumnos: "))


alumnos = {}


for i in range(cantidad):
    nombre = input("Ingrese el nombre del alumno: ")
    nota = int(input("Ingrese la nota de " + nombre + ": "))
    alumnos[nombre] = nota


print("\nNotas de los alumnos:")
for nombre, nota in alumnos.items():
    print(nombre, "tiene la nota de", nota)


suma_notas = sum(alumnos.values())
media = suma_notas / cantidad

print("\nLa media de todas las notas es:", media)