resposta = 'S'

while resposta == 'S':
    n = str(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N]')).upper()
print('FIM')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} impares'.format(par,impar))