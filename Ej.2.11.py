"""Ejercicio 2.11
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga."""

def funcionmas_larga(lista):
	maslarga=""
	for palabra in lista:
		if len(palabra)> len(maslarga):
			maslarga=palabra
	return maslarga

listapalabras=["ordenador","mesa"]

print(funcionmas_larga(listapalabras))