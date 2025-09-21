"""
4. Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
"""


lista_1 = ["Juan", "Luis", "Daniel", "Josias", "Alex"]
print("Lista inicial:", lista_1)


nombre = input("Ingrese el nombre de un estudiante: ")


if nombre in lista_1:
    lista_1.remove(nombre)
    print(f"El estudiante '{nombre}' será eliminado de la lista inicial.")
else:
    print(f"El estudiante '{nombre}' no se encuentra en la lista inicial. Agregamos:")
    lista_1.append(nombre)


print("Lista actualizada:", lista_1)

