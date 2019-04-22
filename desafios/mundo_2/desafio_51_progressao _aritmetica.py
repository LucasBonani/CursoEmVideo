primeiroTermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimoTermo =  + (10 - 1) * razao
for numero in range(primeiroTermo,decimoTermo + razao,razao):
    print('{}'.format(numero), end=' -> ')
print('ACABOU')