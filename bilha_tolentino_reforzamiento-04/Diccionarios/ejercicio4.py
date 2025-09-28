"""
4. Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""
departamentos = { "Lima","Cusco", "Piura", "Arequipa", "Junín", "Puno"}

print("Diccionario inicial:", departamentos)

del departamentos[2]
print("Después de borrar Piura:", departamentos)

departamentos[4] = "La Libertad"
print("Después de actualizar penúltimo:", departamentos)

