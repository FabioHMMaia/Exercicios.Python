# Criar um programa que diga a pessoa o ano em que ela poderá se aposentar. Deve perguntar a pessoa o nome e a idade e criar uma mensagem dizendo em que ano ela poderá se aposentar. 
# Considere que todas as pessoas se aposentam aos 65 anos de idade 

from datetime import datetime #código para importar o ano atual em que estamos

def aposentadoria():
    ano_atual = datetime.now().year #ano atual
    nome = input('Qual seu nome? ') 
    idade = int(input('Qual sua idade? '))
    idadeap = 65 #idade de aposentar

    if idade > idadeap: #Se a pessoa ja estiver na idade avançada É APOSENTADA
        print(f"{nome}, você já está aposentado!")
    elif idade == idadeap: #Se a pessoa acabou de completar 65 ELA PODE SE APOSENTAR 
        print(f"Você já pode se aposentar!")
    else: #Por ultimo se ela tem abaixo de 65 ela tera que se aposentar nesse ano
        somaap = int(idadeap - idade)
        anoap = int(ano_atual + somaap)
        print(f"{nome} poderá se aposentar daqui {somaap} anos.")
        print(f"Se aposentará no ano de {anoap}.")

aposentadoria()