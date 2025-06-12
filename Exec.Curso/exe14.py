# Transforme a temperatura de graus celsius em farenhigth
C = float(input('Digite os graus em Celsius para ver quanto que fica em Farenheit: '))

def CparaF(C):
    F = (C*9/5) + 32
    print(f'{C} graus em Farenheit fica {F}')

CparaF(C)