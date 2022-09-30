'''
Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, 
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
'''

print('Qual largura e altura você deja saber?')

largura = float(input('Digite uma largura: '))
altura = float(input('Digite uma altura: '))

area = largura * altura

lata = area / (2**2)

print('a área a ser pintada é de {}m² e a quantidade de tinta necessária para o serviço é de {} litros.'.format(area,lata))