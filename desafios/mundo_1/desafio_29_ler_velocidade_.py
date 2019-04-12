import random

escolhido = random.randint(50,101)

if escolhido > 80:
    multa = (escolhido - 80) * 7
    print('Você esta acima da velocidade permitida. Sua velocidade é {} e sua multa é de {}'.format(escolhido, multa))
else:
    print('Sua velocidade é de : {}'.format(escolhido))