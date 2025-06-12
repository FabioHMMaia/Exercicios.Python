# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido 
import random

alu1 = input('Nome do primeiro aluno: ')
alu2 = input('Nome do segundo aluno: ')
alu3 = input('Nome do terceiro aluno: ')
alu4 = input('Nome do quarto aluno: ')
alunos = alu1, alu2, alu3, alu4

def sorteio(alunos):
    sorteado = random.choice(alunos)
    print(f'Os alunos que serão sorteados são: {alu1}, {alu2}, {alu3}, {alu4}')
    print(f'O aluno sorteado foi, {sorteado}')

sorteio(alunos)