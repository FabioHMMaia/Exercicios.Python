# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada 

num = int(input('Digite um número: '))
dob = num * 2
tri = num * 3
rq = num ** (1/2)

def function():
    if num > 0 :
        print(f'O dobro de {num} é {dob}, \n O triplo de {num} é {tri}, \n A raiz quadrada de {num} é {rq}')
    else:
        print('Número desconhecido')

function()
