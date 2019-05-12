# dicionários são estruturas de dados semelhantes as listas e tuplas.
# Porém com dicionários temos índices literias (reconhece pelo que está escrito
# não pela posição que se encontra dentro da lista)

# dicionario = {}
# dicionario = dict()

dados = {'nome':'Pedro' , 'idade':33}
print(dados['nome'])
print(dados['idade'])

# append não funciona no dicionário
# para criar novo elemento basta:
dados['sexo'] = 'M' # elemento criado ao final do dicionario existente
print(dados['sexo'])

# uma estrutura de dados 'filmes' com dois elementos
# no Python os elementos são chamados de keys (chaves)
filmes = {'titulo':'Star Wars', 'lancamento':1977, 'diretor':'George Lucas'}
print(filmes)
print(f'O filme {filmes["titulo"]} é o melhor!')
print(filmes.values()) # valores contidos nas chaves
print(filmes.keys()) # chaves para acessar valores
print(filmes.items()) # itens existentes no dicionário
for k,v in filmes.items():
    print(f'O {k} é {v}')
del filmes['lancamento'] # deleta
print(filmes)

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)


