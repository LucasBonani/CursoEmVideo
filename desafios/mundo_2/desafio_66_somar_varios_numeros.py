contador = soma = 0
while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Você digitou {contador} números e a soma entre eles é {soma}')