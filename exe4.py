indice = input('Digite algo: ')

def test():
    if indice.isalnum():
        print('Está correto!')
        print(type(indice))
    else:
        return('Está errado!')

result = test()
