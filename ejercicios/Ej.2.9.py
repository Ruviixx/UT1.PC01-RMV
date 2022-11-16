"""Ejercicio 2.9
Definir un histograma procedimiento() que tome una lista de números enteros e
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
lo siguiente:"""
def procedimiento(lista):
    print("     HISTOGRAMA")
    print("="* 20)
    for item in lista:
         print("X"* item)
    print("="* 20)

procedimiento([4,7,9])

