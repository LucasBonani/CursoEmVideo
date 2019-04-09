# esse tipo de import utiliza somente as funcionalidades chamadas
# from math import sqrt, floor

# esse tipo de import utiliza todas as funcionalidades contidas na biblioteca
import math
# random gera um número aleatório entre 0 e 1
import random
num = int(input('Digite um número: '))
# sqrt serve para cálculo de raiz quadrada
raiz = math.sqrt(num)
# sem formatação
print('A raiz de {} é igual a {}'.format(num, raiz))
# formatando direto no espaço reservado
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
# ceil serve para arredondar para cima
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
# ceil serve para arredondar para baixo
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

numero = random.random()
numero2 = random.randint(1,10)
print(numero2)
print(numero,'e',numero2)