lado01 = int(input('Digite o comprimento do lado 1: '))
lado02 = int(input('Digite o comprimento do lado 2: '))
lado03 = int(input('Digite o comprimento do lado 3: '))

if lado01 == lado02 == lado03:
    print('Equilátero')
elif lado01 != lado02 != lado03:
    print('Escaleno')
else:
    print('Isósceles')