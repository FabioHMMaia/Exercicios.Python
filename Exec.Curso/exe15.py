# Quantos dias ficou com o carro alugado, quantos KM rodou com o carro, Qaunto que ira ter que pagar / Carro R$60 por dia e R$0.15 por KM rodado 
D = int(input('Quantos dias ficou com o carro alugado? '))
KM = float(input('Quantos KM rodou com o carro? '))

def calc(D, KM):
    Dia = D * 60
    Kilo = KM * 0.15
    total = Dia + Kilo
    print(f'O consumidor tera que pagar um valor total de: R${total}')

calc(D, KM)