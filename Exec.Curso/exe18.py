# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input('Digite um ângulo: '))
seno = math.sin(angulo)
cose = math.cos(angulo)
tang = math.tan(angulo)

print(f'O Seno de {angulo} é {seno}. O cosseno de {angulo} é {cose} e a Tangente do {angulo} é {tang} ')