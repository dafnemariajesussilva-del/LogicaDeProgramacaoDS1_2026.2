"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia_total_percorrida = float(input("qual a distancia:"))
total_de_combustivel_gasto = float(input("qual ao total do gasto de combustivel:"))
final = distancia_total_percorrida / total_de_combustivel_gasto
print(f"o consumo medio da motocicleta e: {final:.2f}")