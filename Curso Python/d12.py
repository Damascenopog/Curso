preco = float(input('Digite o preço do produto para calcular o desconta: '))
total = preco - (preco * 5/100)
print('Com o desconto de 5% o produto vai sair por R${:.2f}'.format(total))

