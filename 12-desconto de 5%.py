
'''
Crie um programa que leia o preço de um produto, calcule e mostre o seu 
PREÇO PROMOCIONAL, com 5% de desconto. 
'''

produto = float(input('Digite o preço do produto: '))

preco = produto - (produto * 5/100)

print('O preço promocional é de R${}'.format(preco))