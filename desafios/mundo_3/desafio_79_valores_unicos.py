listaNumeros = list()
while True:
    valorDigitado = int(input('Digite um valor: '))
    if valorDigitado not in listaNumeros:
        listaNumeros.append(valorDigitado)
        print(f'Valor {valorDigitado} adicionado com sucesso!')
    else:
        print(f'Valor {valorDigitado} já existe. Não foi adicionado a lista!')
    simNao = str(input('Quer continuar? [S/N]: '))
    if simNao in 'Nn':
        break
print('-=' * 30)
listaNumeros.sort()
print(f'Você digitou os valores {listaNumeros}')