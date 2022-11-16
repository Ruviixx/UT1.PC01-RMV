"""Ejercicio 2.15
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades."""
contador=0
tupla=(1,1,2,2,4,67,78,55,45,60)
for edad in tupla:
	if edad>20:
		contador=contador +1

print(contador)
