'''
Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em 
R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45. 
'''

pergunta = float(input('Quantos você tem em dolar na sua carteira: '))

mult = pergunta * 5.17

print('você tem em dolar US${} e em rais voce tem R${} na carteira.'.format(pergunta,mult))