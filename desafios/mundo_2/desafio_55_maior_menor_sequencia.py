maiorPeso = 0
menorPeso = 0
for pessoa in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(pessoa)))
    if pessoa == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso foi de {}Kg'.format(maiorPeso))
print('O menor peso foi de {}Kg'.format(menorPeso))