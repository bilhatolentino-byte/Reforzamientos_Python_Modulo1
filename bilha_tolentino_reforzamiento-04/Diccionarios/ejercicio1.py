"""
1. Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal.
"""

persona = { "nombre": "Juan", "edad": 40, "salario": 2800}

print("Diccionario:", persona)


lista_persona = list(persona.values())

print("Lista:", lista_persona)