# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira. EX: Digite um numero: 6.127 o numero tem a parte inteira 6
import math
num = float(input('Digite um número: '))

def function():
    print(f'A parte inteira do número {num} é {math.trunc(num)}' )

function()