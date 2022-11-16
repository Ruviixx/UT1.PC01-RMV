'''
Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3
'''
print("Ejercicio 1.3")
print("********************************")

numeros = range(11)
for i in numeros:
    if i % 3 == 0:
        print(i)
