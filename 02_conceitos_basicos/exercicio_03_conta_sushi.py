"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_total_consumido = float(input("qual valor total:"))
taxa_servico = valor_total_consumido * 0.10
valor_final_conta = valor_total_consumido + taxa_servico
print(f"o valor final da conta a pagar e: R$ {valor_final_conta}:.2f")