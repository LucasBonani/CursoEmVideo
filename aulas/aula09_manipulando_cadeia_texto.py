# técnica de fatiar uma string ou cadeia de carcteres é pegar pedaços dela
# no Python começa contagem de 0

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[13::2])
print(frase[::2])
print(frase[13:4:2])

# técnica de análise é conhecer informações sobre ela. Tamanho, quantidade

print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase))

# técnica de transformação é quando você manipula alterando de alguma forma a string

print(frase.replace('Python','Android')) # replace apenas salva nesta instância
# no exemplo acima seria frase = frase.replace('Python','Android'), assim atribui
print('em' in frase) # valida se existe na frase
print(frase.find('Python')) # aponta a posição

# técnica de divisão refaz o index subdividindo a cadeia de caracteres para uma 'lista'
dividido = frase.split()
print(dividido)
print(dividido[2][3]) # da palavra dois me mostre a letra número 3
# técnica de junção é para juntar os carcteres de um lista

