"""
Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario.
"""
def mostrar_cuadrados(num1, num2):

    for i in range(num1, num2 + 1):
        print("El cuadrado de", i, "es", i**2)


n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))