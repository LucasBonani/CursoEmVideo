# listas [], são mutáveis

lanche = ['hamburger','suco','pizza','pudim']
# aqui  altera par picole
lanche[3]= 'picole'
lanche.append('refrigerante') # append cria novo elemento e add no final da lista
lanche.insert(1,'dogão') # add dogão na posição 1
del lanche[2] # deleta posição 2
lanche.pop(3) # deleta posição 3, geralmente utilizado para deletar o último elemento
lanche.remove('pizza') # remove o elemento que você indicar
print(lanche)

valores = list(range(4,11)) # cria uma lista de estrutura organizada
print(valores)

valor = [2,7,6,34,9,2,1,5]
valor.sort() # ordena a lista
print(valor)

val = [2,6,7,3,34,5,9,0]
val.sort(reverse=True) # ordena do maior para o menor
print(val)

print(len(val)) # saber o tamanho da lista
