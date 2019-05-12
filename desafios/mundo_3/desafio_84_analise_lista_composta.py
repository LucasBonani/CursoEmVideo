pessoas = list()
nomePeso = list()
cont = pessoasPesadas = pessoasLeves = 0

while True:
     nomePeso.append(str(input('Digite o nome: ')))
     nomePeso.append(float(input('Digite peso: ')))
     if len(pessoas) == 0:
          pessoasPesadas = pessoasLeves = nomePeso[1]
     else:
          if nomePeso[1] > pessoasPesadas:
               pessoasPesadas = nomePeso[1]
          if nomePeso[1] < pessoasLeves:
               pessoasLeves = nomePeso[1]
     pessoas.append(nomePeso[:])
     nomePeso.clear()
     cont += 1

     simNao = str(input('Deseja continuar? [S/N]: '))
     if simNao in 'Nn':
          break

print(f'São {cont} cadastradas na lista')
print(f'São {len(pessoas)} cadastradas na lista')
print(f'O maior peso foi {pessoasPesadas}Kg de ', end='')
for p in pessoas:
     if p[1] == pessoasPesadas:
          print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi {pessoasLeves}Kg de ', end='')
for p in pessoas:
     if p[1] == pessoasLeves:
          print(f'{p[0]}', end='')
