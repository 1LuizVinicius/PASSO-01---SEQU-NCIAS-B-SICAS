'''
Desenvolva um programa que leia uma distância em metros e mostre os 
valores relativos em outras medidas. 
Ex: 
Digite uma distância em metros: 185.72 A 
distância de 85.7m corresponde a:
    0.18572Km   1857.2dm 
    1.8572Hm    18572.0cm 
    18.572Dam   185720.0mm
'''

print("Digite uma distância em metros")

metros = float(input("Qual é a distância?: "))

mult = metros * 100

print('a distancia em metros é',mult,'cm.')