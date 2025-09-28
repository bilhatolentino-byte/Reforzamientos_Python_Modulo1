"""
3. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes.
"""
persona = { "nombre": "Juan", "edad": 40, "salario": 2800, "DNI": "87654311"}

lista_persona=list(persona.values())
print(lista_persona)

print(type(lista_persona))