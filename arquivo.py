import math

print("Bem vindo a Mix Tintas!")

area_total = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

cobertura_tinta_quadrado = 3

litros_por_lata = 18

valor_lata = 80

quantidade_tinta_litros = area_total / cobertura_tinta_quadrado

quantidade_latas = math.ceil(quantidade_tinta_litros / litros_por_lata)

custo_total = quantidade_latas * valor_lata

print("Você precisará de", quantidade_latas, "latas de tinta.")
print("O custo total será de R$", custo_total)
