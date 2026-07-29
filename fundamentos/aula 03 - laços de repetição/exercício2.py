populacaoAtual = float(input("Digite a população atual: "))
taxaCrescimento = 0.89
populacaoEstimada = 0.0

for anos in range(1, 26):
    populacaoEstimada += (populacaoAtual * taxaCrescimento) + populacaoAtual

    print(f"A população estimada para o ano {anos} é: {populacaoEstimada:.3f}")