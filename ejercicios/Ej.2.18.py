"""Ejercicio 2.18
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400"""

def es_bisiesto(anio):
	if anio %4==0:
		if not anio %100==0:
			print("es bisiesto")
	else:
		print("no es bisiesto")

es_bisiesto(240)