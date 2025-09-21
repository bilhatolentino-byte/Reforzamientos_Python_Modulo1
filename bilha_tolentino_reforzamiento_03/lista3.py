"""
3. Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""
lista_1=[]
print("lista vacia:", lista_1)
lista_1.append(10)
lista_1.append(20)
lista_1.append(1)
lista_1.append(10)
lista_1.append(15)
lista_1.append(20)
lista_1.append(25)
lista_1.append(30)
lista_1.append(35)
lista_1.append(40)
lista_1.append(45)
lista_1.append(50)
print("lista actualizada:", lista_1)

suma = sum(lista_1)
media = suma / len(lista_1)


print("Lista:", lista_1)
print("Suma de los números:", suma)
print(f"Media de los números: {media:.2f}")

