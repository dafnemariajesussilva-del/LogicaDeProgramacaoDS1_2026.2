"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
pares = 0
for i in range(5):
    numero = int(input("digite um numero inteiro: "))
    if numero % 2 == 0:
        pares += 1
print("quantidade de numeros pares: " , pares)