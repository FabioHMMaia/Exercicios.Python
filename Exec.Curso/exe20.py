# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunose mostre a ordem sorteada
import random

alunos = [] #Lista de alunos vazia

for i in range(4): #Para escrever os nomes
    nome = input(f'Digite o nome do aluno: {i+1}')
    alunos.append(nome) #Adicionar cada nome na lista de alunos

def sorteio(alunos):
    random.shuffle(alunos) #embaralha a lita original 
    print(f'A ordem sorteada para apresentar o trabalho é: ')
    for i, alunos in enumerate(alunos):
        print(f'{i+1} = {alunos}')

sorteio(alunos)
