while True:
    tabuada = int(input('Digite um número para saber a tabuada: '))
    if tabuada < 0:
        print('Você digitou um número negativo, use um positivo')
        break
    for valor in range(1,11):
        print(f'{tabuada} X {valor} = {tabuada*valor}')