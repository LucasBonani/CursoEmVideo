km = float(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dias alugados: '))
valor = (dias * 60) + (km * 0.15)
print('O total a pagar é: R${}'.format(valor))
