import random

list = [1,2,3,4,5]
escolhido = random.choice(list)

chute = int(input('Estou pensando de em número de 1 à 5. Adivinhe qual é: '))

if escolhido == chute:
    print('Acertou miserávi!!!')
else:
    print('Errroouuuu! O número que eu pensei era {}'.format(escolhido))