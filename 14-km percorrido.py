'''
A locadora de carros precisa da sua ajuda para cobrar seus serviços. 
Escreva um programa que pergunte a quantidade de Km percorridos por um carro 
alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço 
total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
'''

print('LOCADORA DE CARROS')

dia = int(input('Por quantos dias você alugou o carro?: '))

km = float(input('Quantos KM você percorreu com o carro?: '))

mult = dia * 90

mult1 = km * 0.20

soma = mult + mult1

print('Você esta devendo R${} para a locadora.'.format(soma))