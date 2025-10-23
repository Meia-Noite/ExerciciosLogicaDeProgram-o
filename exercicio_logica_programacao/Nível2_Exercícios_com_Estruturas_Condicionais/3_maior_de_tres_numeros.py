num01 = int(input('Digite o primeiro número: '))
num02 = int(input('Digite o segundo número: '))
num03 = int(input('Digite o terceiro número: '))

if num01 > num02 and num01 > num03:
    print('O maior número é o ', num01)
elif num02 > num01 and num02 > num03:
    print('O maior número é o ', num02)
elif num03 > num01 and num03 > num02:
    print('O maior número é o ', num03)
if num01 == num02 == num03:
    print('Os números são iguais!')

