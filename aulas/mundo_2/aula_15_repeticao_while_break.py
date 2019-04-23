n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale: {}'.format(s))

# FORMAS DE COMANDO FSTRINGS A PARTIR DO PYTHON 3
# exemplo de f string
print(f'A soma vale: {s}')

nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos')