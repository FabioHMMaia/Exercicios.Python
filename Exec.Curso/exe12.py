# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto 
item = str(input('Qual item quer verificar o preço? '))
prod = float(input('Qual é o preço do produto? R$'))
desc = 0.05
pref = prod - desc

print(f'O preço do(a) {item} é R${prod:.3f}, com um desconto de 5% fica R${pref:.3f}')