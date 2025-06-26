# Crie um programa que leia o nome completo de uma pessoa e mostre na tela
# O nome com todas as letras MAIUSCULAS
# O nome com todas as letras minusculas 
# Quantas letras tem ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome 

nome = input("Digite seu nome: ").strip()

def analisandonome(nome):
    print(nome.upper())
    print(nome.lower())
    print(len(nome.replace(" ", "")))
    print(len(nome.split()[0]))

analisandonome(nome)