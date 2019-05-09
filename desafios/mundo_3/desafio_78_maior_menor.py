valores = []
maior = menor = 0
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'O maior valor digitado foi {maior} na posição ', end='')
for posicao, elementoList in enumerate(valores):
    if elementoList == maior:
        print(f'{posicao}', end='')

print(f'\nO menor valor digitado foi {menor} na posição ', end='')
for posicao, elementoList in enumerate(valores):
    if elementoList == menor:
        print(f'{posicao}', end='')

