# () = tuplas [] = listas {} = dicionario que são variáveis compostas
# ou seja, possuem mais de um elementos
# tuplas são imutáveis, ou seja, não tem como trocar os elementos existentes na tupla



pessoa = ('Lucas', 29, 'M', 99.88)# tuplas no python aceitam dados de tipos diferentes diferentes
# del(pessoa) apaga
print(pessoa)


lanche = ('hamburger', 'suco' , 'pizza' , 'pudim') # estrutura composta
print(lanche)
print(lanche[-2])
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])


for cont in range(0,len(lanche)):
    print(lanche[cont])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0,len(lanche)):
    print(lanche[cont], f'na posição {cont}', )

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) # para ordenar

a = (2, 5, 6)
b = (1,5,8,4, 7)
c = a + b
print(c)
print(c.count(5))
print(c.count(7)) # mostra quantas vezes se repete
print(c.index(5)) # mostra em qual posição está pegando a primeira ocorrencia caso tenha outro igual



