from random import randint

vitoria = 0

print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    valorJogador = int(input('Digite um valor: '))
    escolhidoPc = randint(0, 10)
    total = valorJogador + escolhidoPc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou IMPAR? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {valorJogador} e o computador {escolhidoPc} Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    else:
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes')