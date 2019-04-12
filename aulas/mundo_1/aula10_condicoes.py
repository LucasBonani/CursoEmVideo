# CONDIÇÃO COMUM
tempo = int(input('Quanto tempo tem seu carro? : '))
if tempo <= 3:
    print('CARRO NOVO')
else:
    print('LATA VELHA')
print('-'*5,'FIM','-'*5)

# CONDIÇÃO SIMPLIFICADA
tempo = int(input('Quanto tempo tem seu carro? : '))
print('CARRO NOVO' if tempo <= 3 else 'LATA VELHA')
print('-'*5,'FIM','-'*5)