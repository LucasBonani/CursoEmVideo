pessoas = [['Pedro',25],['Maria',29],['João',21]] # lista composta (lista dentro de lista)
# [2] = lista posição 2 / [0] = João
print(pessoas[2][0])
print(pessoas[1][1])
print(pessoas[0])

# lista simples
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

# lista composta
galera = list()
galera.append(teste[:])
print(galera)

teste[0] = 'Maria'
teste[1] = 22
# [:] = cópia
# sem '[:]' liguarei as duas estruturas
galera.append(teste[:])
print(f' Aqui temos {galera} como estruturas ligadas')

for lista in pessoas: # aqui sai lista completa
    print(lista)

for lista in pessoas: # aqui sai nomes
    print(lista[0])

for lista in pessoas: # aqui sai idade
    print(lista[1])

gente = list()
dado = list()
for cont in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gente.append(dado[:])
    dado.clear()
print(gente)
for p in gente:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')



