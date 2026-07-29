for item in range(6):

    print("---------------------------------")
    print(f"Informações do Aluno {item}")

    nomeAluno = input("Digite o nome do aluno: ")
    notaAluno = float(input(f"Digite a nota do aluno {nomeAluno}: "))

    if notaAluno >= 5.0:
        print(f"O aluno {nomeAluno} está aprovado(a)!")
    else:
        print(f"O aluno {nomeAluno} está reprovado(a).")