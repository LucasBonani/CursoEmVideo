totalCompra = quantidadeProdutoMil = valorProdutoBarato  = contador = 0
nomeProdutoBarato = ''
while True:
    nomeProduto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    contador += 1
    totalCompra += preco
    if preco > 1000:
        quantidadeProdutoMil += 1
    if contador == 1:
        nomeProdutoBarato = nomeProduto
        valorProdutoBarato = preco
    else:
        if preco < valorProdutoBarato:
            nomeProdutoBarato = nomeProduto
            valorProdutoBarato = preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi de R$ {totalCompra}')
print(f'Temos {quantidadeProdutoMil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nomeProdutoBarato} que custa R$ {valorProdutoBarato}')
