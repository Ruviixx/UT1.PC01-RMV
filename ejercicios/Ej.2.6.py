'''Ejercicio 2.6
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la
cadena "estoy probando" debería devolver la cadena "odnaborp yotse'''
def inversa(texto):
    textoinvertido=""
    for i in texto:
        textoinvertido=i+textoinvertido
    return(textoinvertido)
print(inversa("odnaborp yotse"))