# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.

#solicita ao usuario digitar um numero inteiro
numero = int(input('digite um numero inteiro: '))

#verificar se o numero é positivo ou negativo
print(numero, 'é um numero', 'positivo.' if numero >= 0 else 'negativo.')
