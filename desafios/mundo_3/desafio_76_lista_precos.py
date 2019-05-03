listagem = ('lápis', 1,
            'borracha', 2,
            'caderno', 15.50,
            'mochila', 50,
            'canetas', 1.75)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]:>7.2f}')