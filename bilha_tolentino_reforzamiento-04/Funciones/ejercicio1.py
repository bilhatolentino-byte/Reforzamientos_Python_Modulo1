"""
1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente.
"""
def suma_digitos(numero):
    suma = 0
    for digito in str(numero):   # Convertimos a string para recorrer cada dígito
        suma += int(digito)      # Lo volvemos número y lo sumamos
    return suma


num1 = int(input("Ingrese el primer número positivo: "))
num2 = int(input("Ingrese el segundo número positivo: "))


suma1 = suma_digitos(num1)
suma2 = suma_digitos(num2)


if suma1 > suma2:
    print("El número con mayor suma de dígitos es:", num1, "(", suma1, ")")
elif suma2 > suma1:
    print("El número con mayor suma de dígitos es:", num2, "(", suma2, ")")
else:
    print("Ambos tienen la misma suma de dígitos:", suma1)


if suma1 < 10:
    print(num1, "tiene suma de dígitos menor que 10")
if suma2 < 10:
    print(num2, "tiene suma de dígitos menor que 10")