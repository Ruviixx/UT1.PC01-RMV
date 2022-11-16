def max_de_tres(numero1,numero2,numero3):
    if numero1>numero2:
        maximo=numero1
    else:
        maximo=numero2

    if maximo<numero3:
        maximo=numero3

    return maximo
print(max_de_tres(5,6,8))