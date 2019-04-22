maiorIdadeHomem = 0
totalMulherMenosVinteAnos = 0
somaIdade = 0
for pessoa in range(1,5):
    print('-'*5,'{}ª PESSOA'.format(pessoa),'-'*5)
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO: [M/F]: ')).strip()

    somaIdade += idade

    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeDoMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulherMenosVinteAnos += 1

print('A média da idade do grupo é {} anos'.format(somaIdade/4))
print('O {} é o homem mais velho e tem {} anos'.format(nomeDoMaisVelho,maiorIdadeHomem))
print('O total de mulheres com menos de 20 anos é: {}'.format(totalMulherMenosVinteAnos))
