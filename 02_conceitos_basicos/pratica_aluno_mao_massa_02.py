# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor_da_conta = float(input("digite o valor da conta: "))
leia__numero_de_pessoas = float(input("digite o numero de pessoas: "))
calcule_valor_por_pessoa = valor_da_conta / leia__numero_de_pessoas
print(f"esse e o valor pago por pessoa {calcule_valor_por_pessoa:.2f}")

