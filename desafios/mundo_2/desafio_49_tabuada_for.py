numero = int(input('Digite um número para ver a tabuada: '))
for valor in range(1,11):
    print('{} X {} = {}'.format(numero,valor,numero*valor))
