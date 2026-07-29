totalTelevisores = 0.0

for televisores in range(1, 13):

    print("---------------------------------")
    
    valorTelevisor = float(input(f"Digite o valor do televisor do mês {televisores}: "))
    totalTelevisores += valorTelevisor

print(f"A média do valor dos televisores vendidos nos últimos 12 meses é: R$ {totalTelevisores / 12:.2f}")
