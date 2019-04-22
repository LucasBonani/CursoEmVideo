from datetime import date

totalMaior = 0
totalMenor = 0
anoAtual = date.today().year

print('O ano em que estamos é {}!'.format(anoAtual))

for pessoa in range(1,8):
    anoNascimento = int(input('Em que ano a {}º pessoa nasceu? '.format(pessoa)))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor +=1
print('Tivemos um total de {} pessoas maiores de idade\nE um total de {} pessoas menores de idade.'
      .format(totalMaior,totalMenor))

