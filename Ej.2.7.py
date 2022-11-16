"""Ejercicio 2.7
Definir una función superposicion() que tome dos listas y devuelva True si tienen al
menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
el bucle for anidado."""

def superposicion(lista1,lista2):
    repetido=False
    for item1 in lista1:
        for item2 in lista2:
            if item1==item2:
                repetido=True
    return repetido
lista1=[0,2,3,4]
lista2=[1,5,6,7]
resultado=superposicion(lista1,lista2)
print(resultado)