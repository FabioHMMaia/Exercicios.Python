nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

def vida(nome, idade):
    if(idade < 18):
        return(print(f"{nome} é criança!"))
    elif(idade >=  65 ):
        return(print(f"{nome} é idoso(a)!"))
    else:
        return(print(f"{nome} é adulto!"))

result = vida(nome, idade)
