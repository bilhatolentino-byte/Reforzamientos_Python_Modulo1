"""
Escribe un programa que convierta cierta cantidad de soles a
dólares, usando un tipo de cambio que se proporciona en el
programa.
Estos valores estarán dentro de sus variables respectivamente.
La salida mostrará tres cambios que hagas respectivamente de
tres montos a convertir.
"""

tipo_cambio = 3.85

monto_1 = 100
monto_2 = 250
monto_3 = 500


dolares_1 = monto_1 / tipo_cambio
dolares_2 = monto_2 / tipo_cambio
dolares_3 = monto_3 / tipo_cambio

# Salida
print(f"{monto_1} soles es igual a: ${dolares_1:.2f} dólares")
print(f"{monto_2} soles es igual a: ${dolares_2:.2f} dólares")
print(f"{monto_3} soles es igual a: ${dolares_3:.2f} dólares")