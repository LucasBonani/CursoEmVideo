for c in range(1,6): # contagem normal
    print(c)
print('FIM')
for d in range(6,0,-1): # de 6 a 0
    print(d)
print('FIM')
for e in range(0,7,2): # de 0 a 7 pulando de dois em dois
    print(e)
print('FIM')

n = int(input('Digite um número: '))
for c in range(1,n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for a in range(i, f+1, p):
    print(a)
print('FIM')

s=0
for h in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma de todos os números é {}'.format(s))