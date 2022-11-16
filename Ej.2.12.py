"""Ejercicio 2.12
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres."""
def filtrar_palabras(lista,entero):
    listaresultado=[]
    for palabra in lista:
        if len(palabra) >= entero:
            listaresultado.append(palabra)
    return listaresultado
l=["alberto","suspenso","mesa"]
print(filtrar_palabras(l,5))
