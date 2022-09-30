'''
Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o 
seu novo salário, com 15% de aumento.
'''

salario = int(input("Qual seu salario?: "))

promocao = salario + (salario*15 / 100)


print(f"seu salario e de {salario} voce tera um aumeto de 15%, seu novo salario sera {promocao}.")