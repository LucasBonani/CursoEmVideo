# O ideal é criar funções para as rotinas
# rotinas são códigos que se tornam repetitivos ou de uso comum em diversos pontos do projeto
# def = funções e todas as funções no python são terminadas em ()
# deve haver dois espaços entre a def e o código principal

print('-='*8)
print('CURSO EM VÍDEOS')
print('-='* 8)


def linha():
    print('-='*16)
# deve haver dois espaços entre a def e o código principal
# deve haver dois espaços entre a def e o código principal
linha()
print('CURSO EM VÍDEO DENTRO DA FUNÇÃO')
linha()


def exemplo(mensagem): # o que há dentro de () é chamado de parâmetro
    linha()
    print(mensagem)
    linha()


exemplo('CURSO EM VÍDEO DENTRO DA FUNÇÃO COM PARÂMETRO')


