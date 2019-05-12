# empacotamento de parâmetros ou empacotar parâmetros

#aqui você poderá passar diversos parâmetros, característica do Python
def contador(*num): # '*' é o desempacotador
    tam = len(num)
    print(f'Recebi os valores {num} e são do tamanho de {tam} números na memória')

contador(1,4,5,7,8,9)
contador(3,6,7)


valores = [2,5,6,7]
print(f'Lista "valores" ANTES de passar por "def dobra": {valores}')
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        # aqui recebe o dobro do valor encontrado na determinada posição da lista
        lista[posicao]*=2
        posicao+=1


dobra(valores)
print(f'Lista "valores" DEPOIS de passar por "def dobra": {valores}')


def soma(*valores):
    resultado = 0
    for numero in valores:
        resultado += numero
    print(f'Somando os valores {valores} temos o resultado: {resultado}')


soma(1,5,6,8,9)
soma(1,2,3)