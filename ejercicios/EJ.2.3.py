'''Ejercicio 2.3
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
que python tiene la función len() incorporada, pero escribirla por nosotros mismos
resulta un muy buen ejercicio.'''

def longitud_lista(lista):
    longitud=0
    for i in lista:
        longitud=longitud +1
    return longitud
lista1=[2,3,4,5,6,7,8,2]
a=longitud_lista(lista1)
print(a)



