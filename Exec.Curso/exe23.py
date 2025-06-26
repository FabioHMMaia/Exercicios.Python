# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Exe: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um numero inteiro: '))

def analisandoNum(numero):
    numero_str = f"{numero:04d}" #Garante que o numero terá 4 digitos
    print('Unidade: ',numero_str[3])
    print('Dezena: ',numero_str[2])
    print("Centena: ",numero_str[1])
    print("Milhar: ",numero_str[0])

analisandoNum(numero)
