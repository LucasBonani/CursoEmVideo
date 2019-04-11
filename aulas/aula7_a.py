print('='*20)

nome = input('Qual o seu nome? ')
#alinhado a direita
print('Prazer em te conhecer {:>20} !'.format(nome))
#alinhado a esquerda
print('Prazer em te conhecer {:<20} !'.format(nome))
#centralizado
print('Prazer em te conhecer {:^20} !'.format(nome))
#centralizado com = em 20 caracteres
print('Prazer em te conhecer {:=^20} !'.format(nome))
n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisão'
      ' é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira é {} e potência é {}'.format(di, e))


