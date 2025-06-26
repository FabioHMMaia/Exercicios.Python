#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nomeCidade = input("Digite o nome de uma cidade: ")

def analisandoCidade(nomeCidade):
    if(nomeCidade.startswith("Santo")): #Faz analisar se começa com Santo ou não
        print('Essa cidade começa com Santo',)
    else:
        print('Essa cidade não começa com Santo')

analisandoCidade(nomeCidade)