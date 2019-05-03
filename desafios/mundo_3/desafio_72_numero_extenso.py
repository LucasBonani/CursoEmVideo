numTupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',)
while True:
    numero = int(input('Digite um número entre 0 e 10: '))
    if 0 <= numero <= 10:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou {numTupla[numero]}')
