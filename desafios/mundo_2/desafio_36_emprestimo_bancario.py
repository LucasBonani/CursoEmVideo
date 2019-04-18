valorCasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = float(input('Em quantos anos pretende pagar? '))

meses = anos * 12
prestacao = valorCasa / meses

if prestacao > salario * 0.30:
    print('Seu empréstimo foi negado')
else:
    print('Parabéns seu empréstimo foi aprovado!')
