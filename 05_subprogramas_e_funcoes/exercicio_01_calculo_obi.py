"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuação_total(fase1, fase2, fase3):
    pontuação_total = (fase1 + fase2 + fase3)
    return pontuação_total
total = calcular_pontuação_total(10, 7, 9)
print(f"\nA pontuação total e de: {total} pontos")