# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa 
import math 

c_o = float(input('Digite o comprimento do Cateto Oposto: ')) #Cateto Oposto
c_a = float(input('Digite o comprimento do Cateto Adjacente: ')) #Cateto Adjacente 

hipotenusa = math.hypot(c_o,c_a) #Calculo da Hipotenusa

print(f'O calculo da Hipotenusa é {hipotenusa}')