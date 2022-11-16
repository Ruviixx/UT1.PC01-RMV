#Ejercicio 1.1
'''
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor desconocido
'''
print("Ejercicio 1.1")
nota=10
print("La nota proporcionada ha sido ",nota)
if nota <6:
    nota="F"
elif nota <7 and nota >= 6:
    nota="E"
elif nota >7 and nota <= 8:
    nota="D"
elif nota >8 and nota<=9:
    nota="B"
elif nota>9 and nota<=10:
    nota="A"

print("La nota final ha sido ",nota)
