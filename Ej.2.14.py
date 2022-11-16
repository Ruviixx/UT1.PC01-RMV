"""Ejercicio 2.14
Construir un pequeño programa que convierta números binarios en enteros.
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

print ("Introduce el numero binario que quieres convertir a entero")

numero_bin = input()
numero_decimal = 0
valor_string = str(numero_bin)

posicion = len(numero_bin) - 1

for posicion, digito_string in enumerate (numero_bin[::-1]):
    digito = int(digito_string)
    print (f'digito: {digito}, posicion:{posicion}')

for posicion, digito_string in enumerate (numero_bin[::-1]):
    numero_decimal += int(digito_string) * 2 ** posicion

print (f'El número decimal que buscamos es {numero_decimal}')