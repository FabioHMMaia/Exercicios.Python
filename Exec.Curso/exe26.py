# Faça um programa que leia uma frase pelo teclado e mostre
# Quantas vezes aparece a letra "a"
# Em que posição aparece ela a primeira vez
# Em que posição aparece ela na ultima vez

frase = input("Digite uma frase qualquer: ").lower().strip()#Sempre colocar isso 

def analisafrase(frase):
    contarA = frase.count('a')
    if(contarA > 0 ):
        print(f'Na frase tem {contarA} "a" ')
        primeira = frase.find('a') + 1 #Para começar a contar a partir do 1 
        ultima = frase.rfind('a') + 1 #Ira começar a ler da direita para esquerda
        print(f'A primeira letra "a" apareceu na posição {primeira}')
        print(f'A ultima letra "a" apareceu na posição {ultima}')
    else:
        print('Não tem a letra "a" na frase')

analisafrase(frase)
