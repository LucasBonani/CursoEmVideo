# modularizar é o ato de construir módulos
# o foco principal é:
# - dividir um programa grande entre suas funcionalidades
# - aumentar a legibilidade dos programas e códigos
# - isso facilita a manutenção do sistema
# - rutilização dos módulos para outros projetos
# - ocultação dos códigos detalhados

# aqui utiliza módulo 'numeros' do pacote 'uteis'
from uteis import numeros as uteis
num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')

num1 = int(input('Digite um numero pra soma: '))
num2 = int(input('Digite um numero pra soma: '))
total = uteis.soma(num1,num2)
print(f'O total da soma é: {total}')


# bibliotecas é chamado em Python de pacotes
# serve quando exitem muitos módulos no seu código,
# onde vc terá várias funções separadas por assuntos, ou seja,
# módulos equivalentes unidos nas funções dentro dos pacotes




