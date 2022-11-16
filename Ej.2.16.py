"""Ejercicio 2.16
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)
"""
lista=["ruben","alberto","guille"]
contador=0
for nombre in lista:
	if nombre[0]=="a":
		contador=contador +1
print(contador)
