# Solicita os dados do aluno
nomeAluno = input("Digite o nome do aluno: ")
notaAluno = float(input(f"Digite a nota do aluno {nomeAluno}: "))

# Verifica se o aluno está aprovado ou reprovado
if notaAluno >= 5.0:
    print(f"O aluno {nomeAluno} está aprovado(a)!")
else:
    print(f"O aluno {nomeAluno} está reprovado(a).")