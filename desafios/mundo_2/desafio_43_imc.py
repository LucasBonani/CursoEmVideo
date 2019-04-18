peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * 2)

if imc <= 18.5:
    print('Você está abaixo do seu peso ideal! Seu imc é: {:.2f}')
elif imc > 18.5 and imc < 25:
    print('Parabéns, você está no seu peso ideal! Seu imc é: {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso! Tente emagrecer um pouco! Seu imc é: {:.2f}'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seguinte, você está obeso...vá emgrecer!! Seu imc é: {:.2f}'.format(imc))
elif imc > 40:
    print('Você está com obesidade móbida....Homer Simpson! Seu imc é: {:.2f}'.format(imc))
