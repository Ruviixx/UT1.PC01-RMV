"""Ejercicio 2.13
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""
palabra=input("Escribe una cadena ")
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
contador=0
for letra in palabra:
    if letra in mayus:
        contador=contador +1
print(contador)

