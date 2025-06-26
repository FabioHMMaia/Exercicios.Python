# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

nome = input('Digite seu nome completo: ')

def analisandoNome(nome):
    if('silva' in nome.lower()):
        print('Existe o sobrenome Silva no nome')
    else:
        print('Não existe o sobrenome Silva no nome')

analisandoNome(nome)