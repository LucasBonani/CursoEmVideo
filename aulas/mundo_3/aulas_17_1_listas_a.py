valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c ,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

# O PYTHON CRIA LIGAÇÃO ENTRE LISTAS QUANDO VC ATRIBUI IGUALDADE
a = [1,2,3,4,]
b = a
print(f'Lista A1: {a}')
print(f'Lista B1: {b}')

# alterando as listas
b[2] = 9
print(f'Lista A2: {a}')
print(f'Lista B2: {b}')

c =a[:] # aqui c recebe todos os itens de a (isto é uma cópia)
c[1] = 5
print(f'Lista A: {a}')
print(f'Lista C: {c}')