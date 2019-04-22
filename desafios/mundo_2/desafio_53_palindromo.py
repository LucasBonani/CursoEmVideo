frase = str(input('Digite algo e descubra se é um palíndromo: ')).strip().upper()
print(frase)
#strip tira espaços antes e depois da frase e upper para miusculo
palavras = frase.split() #reserva cada palavra separada num array
print('Tudo separado: {}'.format(palavras))
junto = ''.join(palavras) # junta palavras numa só
print('Tudo junto: {}'.format(junto))
inverso = junto[::-1] # aqui inverte usando Técnica de Fatiamento
'''for letra in range(len(junto) - 1, -1, -1): #aqui inverte a palavra usando for
    inverso += junto[letra]'''
if inverso == junto:
    print('O que foi digitado é um palíndromo: {} = {}'.format(inverso,junto))
else:
    print('O que foi digitado NÃO é um palíndromo: {} = {}'.format(inverso,junto))

