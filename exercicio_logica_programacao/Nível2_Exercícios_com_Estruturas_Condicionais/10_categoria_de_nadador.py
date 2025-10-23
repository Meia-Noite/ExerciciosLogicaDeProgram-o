idade = int(input('Digite sua idade: '))

if idade <= 10:
    print('Categoria: infantil')
elif (idade >= 11) and (idade <= 17):
    print('Categoria: Juvenil')
else:
    print('Categoria: Adulto')