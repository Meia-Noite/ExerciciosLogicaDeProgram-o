print('==========================')
print('= Calculador de Desconto =')
print('==========================')

preco = int(input('Digite o preço do produto: '))
desconto = int(input('Digite a porcentagem de desconto: '))

total = preco - (preco * (desconto / 100))

print(total)