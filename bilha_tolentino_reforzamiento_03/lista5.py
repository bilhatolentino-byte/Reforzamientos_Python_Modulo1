"""
5. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de TI)
y harás una copia donde adrede agregarás nombres que estarán repetidos
(mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista inicial
"""

companias = []


tam = int(input("Ingrese el tamaño de la lista: "))


for i in range(tam):
    nombre = input("Ingrese una compañía TI: ")
    companias.append(nombre)

print("Lista inicial:", companias)


companias_repetidas = companias.copy()


extra = int(input("Cantidad de nombres repetidos a agregar: "))
for i in range(extra):
    nombre = input("Ingrese un nombre repetido o nuevo: ")
    companias_repetidas.append(nombre)

print("Lista con repetidos:", companias_repetidas)


companias_unicas = []
for nombre in companias_repetidas:
    if nombre not in companias_unicas:
        companias_unicas.append(nombre)

print("Lista sin repetidos:", companias_unicas)