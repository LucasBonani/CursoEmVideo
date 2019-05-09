listaValores = []

for cont in range(0,5):
    valorDigitado = int(input('Digite um valor: '))
    # se valor digitado for o primeiro ou for maior que o último elemento da lista
    if cont == 0 or valorDigitado > listaValores[-1]:
        listaValores.append(valorDigitado)
        print(f'Valor {valorDigitado} adicionado ao final da lista')
    else:
        posicao = 0
        # verifica da posição zero até a última posição da lista
        # para inserir na posição correta
        while posicao < len(listaValores):
            # verifica se valor digitado é <= a cada uma das posições
            # de valores já existente na lista
            if valorDigitado <= listaValores[posicao]:
                # insere o valor digitado na posição específicada
                # já validado no passo anterior
                listaValores.insert(posicao, valorDigitado)
                print(f'Valor {valorDigitado} adicionado na posição {posicao}')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {listaValores}')