# Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário com 15% de aumento 

salario = float(input('Qual o seu salário: R$'))
aumento = 0.15
salariof = salario * aumento + salario

print(f'O salario é de R${salario} com o aumento de 15% ficou em R${salariof}')