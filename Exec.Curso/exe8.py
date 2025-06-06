# Escreva um programa que leia um valor em metros e exiba convertendo em centimetros e milimetros

metros = float(input('Digite um valor em metros: '))
centi = metros * 100
milime = metros * 1000

def function():
    if metros < 0:
        print('Calculo não sucedido')
    else:
        print(f'O valor em metros é {metros}\nO valor em centímetros é {centi}\nO valor em milímetros é {milime}')
    
function()