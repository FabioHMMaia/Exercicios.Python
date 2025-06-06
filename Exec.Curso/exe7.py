# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média 

nota1 = int(input('Digita sua nota 1: ')) 
nota2 = int(input('Digite sua nota 2: '))
media = (nota1 + nota2)/2

def function():
    if nota1 < 0 or nota2 < 0:
        print('Calculo da média inválido')
    else:
        print(f'O calculo da média das notas {nota1} + {nota2} = {media}')

function()