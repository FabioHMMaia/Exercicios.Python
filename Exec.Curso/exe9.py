# Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

num = int(input('Digite um número: '))
for i in range(1, 11): #Faz com que calcule a tabuada inteira de 1 á 10 
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

