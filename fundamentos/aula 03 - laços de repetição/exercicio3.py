metaMensal = 20.000
quantidadeSemanalMascaras = 0.0
quantidadeTotalMascaras = 0.0

for semana in range(1, 5):
    print("---------------------------------")

    quantidadeSemanalMascaras = float(input(f"Digite a quantidade de máscaras produzidas na semana {semana}: "))

    quantidadeTotalMascaras += quantidadeSemanalMascaras

print(f"A quantidade total de máscaras produzidas no mês foi: {quantidadeTotalMascaras:.3f}")

print(f"A média semanal de máscaras produzidas foi: {quantidadeTotalMascaras / 4:.3f}")

if quantidadeTotalMascaras >= metaMensal:
    print("A meta mensal foi atingida!")


