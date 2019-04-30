idade18 = totalHomens = totalMulher20 = 0
while True:
    print('CADASTRAR UMA PESSOA')
    idade = int(input('IDADE: '))
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulher20 += 1
    simOuNao = ' '
    while simOuNao not in 'SN':
        simOuNao = str(input('Cadastrar outra pessoa? [S/N]')).strip().upper()[0]
    if simOuNao == 'N':
        break
print(f'Total de pessoas maiores de idade são: {idade18}')
print(f'Ao todo temos {totalHomens} homens cadastrados')
print(f'Ao todo temos {totalMulher20} mulheres com menos de 20 anos')
