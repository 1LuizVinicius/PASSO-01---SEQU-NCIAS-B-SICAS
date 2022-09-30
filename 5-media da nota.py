'''
 Faça um programa que leia as duas notas de um aluno em uma matéria e mostre 
na tela a sua média na disciplina. 
Ex: 
Nota 1: 4.5 
Nota 2: 8.5 
A média entre 4.5 e 8.5 é igual a 6.5 
'''

print("Media de notas")

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input("Digite a segunda nota: "))

soma = nota1 + nota2

media = soma/2

print(f"A media das duas notas é {media}")