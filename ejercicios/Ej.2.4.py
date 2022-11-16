'''Ejercicio 2.4
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
contrario devuelve False.
'''
"""
def esvocal(caracter):
    if caracter=="a" or caracter=="e" caracter=="i" 
        return True
    else:
        return False


print(esvocal("i"))

"""


def esvocal(caracter):
    listavocales=["a","e","i","o","u"]
    if caracter in listavocales:
        return True
    else:
        return False

print(esvocal("a"))