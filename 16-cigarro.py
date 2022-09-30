'''
Escreva um programa para calcular a redução do tempo de vida de 
um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos 
ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. 
Calcule quantos dias de vida um fumante perderá e exiba o total em dias. 
'''

nome = input('Qual seu nome?: ')

tempo = int(input('A quanto tempo você fuma?: '))

anos = tempo*365

cigarro = int(input('Quantos cigarro você fuma por dia?: '))

minuto = cigarro * 10

#perda = anos * minuto

print(f'{nome} você perdeu {anos} dias e {minuto} minutos da sua vida!!!')