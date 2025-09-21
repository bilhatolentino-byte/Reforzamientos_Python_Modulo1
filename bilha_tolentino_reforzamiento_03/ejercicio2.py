"""
Crea un programa que calcule el Índice de Masa Corporal
(IMC) de una persona.
La fórmula es:

En el mensaje también indicar el nombre de la persona indicando su
IMC también

"""

nombre = "Juan"
peso = 60       # en kilogramos
estatura = 1.65 # en metros

# Cálculo del IMC
imc = peso / (estatura ** 2)

# Mostrar resultado
print(f" El Índice de Masa Corporal (IMC) es de {nombre} es: {imc:.2f}")