"""
2. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""
persona = { "nombre": "Juan", "edad": 40, "salario": 2800}

persona["dni"] = "87654311"

print("salario", persona["salario"], "y DNI", persona["dni"])

print("diccionario actualizado", persona)
