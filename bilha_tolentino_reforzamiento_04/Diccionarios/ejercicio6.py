"""
6. Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario.
"""
diccionario = {}

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))


diccionario[num1] = num1 ** 3
diccionario[num2] = num2 ** 3
diccionario[num3] = num3 ** 3
diccionario[num4] = num4 ** 3


print("Diccionario con números y sus cubos:", diccionario)
