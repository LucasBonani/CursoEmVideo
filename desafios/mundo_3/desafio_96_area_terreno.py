def area(largura,comprimento):
    resposta = largura * comprimento
    return resposta

largura = float(input('LARGURA (M): '))
comprimento = float(input('COMPRIMENTO (M): '))
print(f'A área de um terreno com {largura} X {comprimento} é de: {area(largura,comprimento)}m².')