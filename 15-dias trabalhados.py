'''
 Crie um programa que leia o número de dias trabalhados em um mês e mostre 
o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha 
R$25 por hora trabalhada. 
'''
dia = float(input('Quantos dias você trabalhou nosse mês?: '))

mult = dia * 8

mult1 = mult * 25

print('Seu salario desse mês é de R${}.'.format(mult1))