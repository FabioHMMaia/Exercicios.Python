#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessário para pinta-la, sabendo que cada litro pinta 2m

larg = float(input('Qual a largura da parede em metros quadrados: '))
alt = float(input('Qual a altura da parede em metros quadrados: '))
area = larg * alt

tinta = area / 2

print(f'A largura é {larg}, a altura é {alt}, então a área fica {area} metros quadrados\nPrecisa de {tinta} litros de tinta para pintar essa área!!')
































