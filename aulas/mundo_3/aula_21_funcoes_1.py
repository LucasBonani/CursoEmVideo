# PARA MANUAL DAS FUNÇÕES VÁ EM: 'Python Console'>>digite a tag 'help()'>>enter
# ou digite a função que você quer entender como funciona.
# Exemplo: help(print) ou print(input.__doc__)

# DOCSTRINGS é uma string de documentações
def contador(i,f,p):
    """
        ->teste de documentação docstring.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c+= p
    print('FIM!')


contador(2,10,2)
help(contador)

# PARÂMETROS OPCIONAIS
def somar(a=0,b=0,c=0): # tudo que está '=0' é pode ou não receber parâmetros (é opcional)
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,2,5)
somar(1,4)
somar()

# ESCOPO DE UMA VARIÁVEL = é onde a variável vai existeir e onde não vai existir

# - escopo global é onde a variável é valida para toda a classe
# - escopo local é onde a variável é valida somente onde foi criada
def teste():
    x = 4 # aqui é uma variável local
    print(f'Na função teste , n vale {n}')
    print(f'Na função teste, x vale {x}')

# Programa Principal
n = 2 # aqui é uma variável global
print(f'No programa principal, n vale {n}')
teste()

def teste(b):
    global a # utiliza variável local como global
    a=10
    b+=4
    c=2
    print(f'Valor de a dentro da função teste = {a}')
    print(f'Valor de b dentro da função teste = {b}')
    print(f'Valor de c dentro da função teste = {c}')


a = 5
teste(a)
print(f'Valor de a fora da função teste = {a}')

# RETORNO DE VALORES COM return
def somar(a=0,b=0,c=0):
    s=a+b+c
    return s


r1 = somar(1,2,3)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cálculos deram: {r1}, {r2}, {r3}')

