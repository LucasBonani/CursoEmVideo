soma = 0
contador = 0

for valor in range(1,7):
    numero = int(input('Digite o {}º valor inteiro: '.format(valor)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('Você informou {} números pares e a soma entre eles é: {}'.format(contador, soma))

