"""
13. Crea un programa que convierta una temperatura en grados Celsius a
Fahrenheit. La fórmula que tiene que tener en cuenta es la siguiente:
F = (C * 9)/5 + 32
Deberá imprimir algo como lo siguiente:
La temperatura en °C: 30
Temperatura en Fahrenheit: 86.00
Realizarlo con dos distintos datos para la temperatura en Celsius (usar dos
variables iniciales para obtener dos temperaturas finales en Fahrenheit)
"""
temp_celcius1=30
temp_celcius2=40

temp_fahrenheit1=(temp_celcius1*9)/5 + 32
temp_fahrenheit2=(temp_celcius2*9)/5+32
#1
print(f"Temperatura en °C(1): {temp_celcius1}")
print(f"Temperatura en Fahrenheit(1): {temp_fahrenheit1:.2f}")
#2
print(f"Temperatura en °C(2): {temp_celcius2}")
print(f"Temperatura en Fahrenheit(2): {temp_fahrenheit2:.2f}")