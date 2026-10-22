"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    litros = distancia_km / consumo_kml
    custo = litros * preco_combustivel
    return custo
def calcular_custo_alimentação(qtd_pessoas, dias, diaria_alimentação):
    custo = qtd_pessoas * dias * diaria_alimentação
    return custo
distancia = float(input("Digite a distancia da viagem em km: "))
consumo = float(input("Digite o consumo do veiculo em km/: "))
preco = float(input("Digite o preço do combustivel por litro: "))

pessoas = int(input("digite a quantidade de pessoas: "))
dias = int(input("digite a quantidade de dias: "))
diaria = float(input("digite o custo diario de alimentação por pessoa: "))

custo_transporte = calcular_custo_transporte(distancia, consumo, preco)
custo_alimentacao = calcular_custo_alimentação(pessoas, dias, diaria )

custo_total = custo_transporte + custo_alimentacao
print(f"Custo do transporte: R$ {custo_transporte:.2f}")
print(f"Custo da alimentação: R$ {custo_alimentacao}")
print(f"Custo total da viagem: R$ {custo_total:.2f}")