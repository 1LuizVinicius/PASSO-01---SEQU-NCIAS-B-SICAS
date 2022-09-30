'''
Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a 
sua terça parte. 
Ex: 
Digite um número: 3.5 
O dobro de 3.5 é 7.0 
A terça parte de 3.5 é 1.16667
'''

print('Qual número você deseja saber o dobro e a terça parte?')
pergunta = float(input('Digite um numero: '))
print('Calculando...')

dobro = pergunta * 2
terca_parte = pergunta / 3

print('O dobro de {} é {}.'.format(pergunta,dobro))
print('e o triplo de {} é {:.5f}.'.format(pergunta,terca_parte))