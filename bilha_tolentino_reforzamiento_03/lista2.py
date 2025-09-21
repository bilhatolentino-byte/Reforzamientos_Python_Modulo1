"""
2. Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""
departamentos = ["Junin", "Cusco", "Huanuco", "Ucayali", "Loreto", "Puno"]

print("Lista de departamentos inicial:")
print(departamentos)

dep1 = input("Ingrese el primer departamento de la lista: ")
dep2 = input("Ingrese un departamento fuera de la lista: ")


if dep1 in departamentos:
    indice = departamentos.index(dep1)
    departamentos[indice] = dep2
    print("\nLista actualizada de departamentos:")
    print(departamentos)
else:
    print(f"\nEl departamento '{dep1}' no se encuentra en la lista.")