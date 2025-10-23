peso = int(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

IMC = peso / (altura * altura )

if IMC < 18.5:
    print(f'Seu IMC é: {IMC:.1f}')
    print('Classificação: Abaixo do peso')
elif IMC == 18.5 or IMC < 25:
    print(f'Seu IMC é: {IMC:.1f}')
    print('Classificação: Peso normal')
elif IMC == 25 or IMC < 30:
    print(f'Seu IMC é: {IMC:.1f}')
    print('Classificação: Sobrepeso')
else:
    print(f'Seu IMC é: {IMC:.1f}')
    print('Classificação: Obesidade')