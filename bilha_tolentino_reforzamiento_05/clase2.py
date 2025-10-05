"""
2. Crear una clase llamada Circulo que contenga radio en su constructor y
que contenga un método área que devuelva el área de un círculo.
Adicionalmente habrá un método que devuelva el perímetro del círculo.
También habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""
import math

class Circulo:
    def __init__(self, radio=0):
        self.radio = radio

    def pedir_radio(self):
        self.radio = float(input("Ingresa el radio del círculo: "))

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

print("Primer círculo:")
c1 = Circulo()
c1.pedir_radio()
print(f"Área: {c1.area():.2f}")
print(f"Perímetro: {c1.perimetro():.2f}")

print("\nSegundo círculo:")
c2 = Circulo(5)
print(f"Radio: {c2.radio}")
print(f"Área: {c2.area():.2f}")
print(f"Perímetro: {c2.perimetro():.2f}")
