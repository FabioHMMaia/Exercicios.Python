# Faça um prgrama que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = input("Digite seu nome completo: ").strip()

def analisanome(nome):
    div = nome.split()
    primeira = div[0] #Zero sempre o primeiro elemento da lista
    ultima = div[-1] #-1 smepre vai ser o ultimo elemento da lista 
    print(f'Nome: {nome}')
    print(f'Primeiro: {primeira}')
    print(f'Ultimo: {ultima}')

analisanome(nome)