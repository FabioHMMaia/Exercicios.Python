# Crie um programa que leia qaunto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 

real = float(input('Quanto de dinheito você tem na carteira: R$'))
dolar = real / 3.27

print(f'Com R${real} você podera obter U${dolar:.2f}') #duas casas flutuantes
