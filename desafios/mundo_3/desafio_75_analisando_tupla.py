numero = (
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: '))
         )
print(f'Você digitou os valores {numero}')
print(f'O valor 9 apareceu {numero.count(9)}')
if 3 in numero:
    print(f'O valor 3 está na {numero.index(3)}ª posição')
else:
    print(f'O valor 3 não foi digitado.')
print('Os números pares digitados foram:', end= ' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
