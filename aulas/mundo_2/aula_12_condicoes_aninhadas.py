nome = str(input('Qual é seu nome? '))
if nome == 'Lucas':
    print('Seu nome é o melhor!!')
elif nome in 'Luciana Thais Clarice Dani':
    print('Que belo nome o seu')
else:
    print('Seu nome é bem comum!')
print('Tenha um bom dia, {}!'.format(nome))
