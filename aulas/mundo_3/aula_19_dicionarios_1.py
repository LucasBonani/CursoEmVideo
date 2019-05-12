estado = dict() # dicionario
brasil = list() # lista

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # copy() equivale [:]
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()