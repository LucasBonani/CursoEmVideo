import time
import emoji

# contagem regressiva
for contagem in range(10,0,-1):
    print(contagem, end=' ')
    time.sleep(1)
print(emoji.emojize(':tada: :boom: FELIZ ANO NOVOOOO!!!! :boom: :tada:', use_aliases=True))

# todos os números pares entre 1 e 50
for numeros in range(1,51):
    if numeros % 2 == 0:
        print(numeros, end=' ')
print('FIM')