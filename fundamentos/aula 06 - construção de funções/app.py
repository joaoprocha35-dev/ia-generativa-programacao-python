# Importa o módulo de utilidades
import utilidades

# Laço de Repetições
while True:

    print("Opções disponíveis:")
    print("1 - Calcular a área de um retângulo")
    print("2 - Calcular a área de um círculo")
    print("3 - Calcular a área de um triângulo")

    resposta = int(input("Digite a opção desejada: "))


    if (resposta == 1):
        # Solicita para o usuário a base e a altura de um retângulo
        base = float(input("Digite a base de um retângulo (cm): "))
        altura = float(input("Digite a altura de um retângulo (cm): "))

        # Faz o cálculo da área usando a função do módulo de utilidades
        resultadoRetangulo = utilidades.calcular_area_retangulo(base, altura)
        print(f"Área do retângulo: {resultadoRetangulo} cm²")

    elif (resposta == 2):

        # Solicita para o usuário o valor do raio do círculo
        raio = float(input("Digite o valor do raio do círculo: "))

        #Faz o cálculo da área do círculo utilizando a função do módulo de utilidades
        resultadoCirulo = utilidades.calcular_area_circulo(raio)

        print(f"Área do círculo: {resultadoCirulo} cm²")

    elif (resposta == 3):
        # Solicita para o usuário a altura do triângulo
        altura = float(input("Digite o valor da altura do triângulo: "))

        # Solicita para o usuário a base do triângulo
        base = float(input("Digite o valor da base do triângulo: "))

        #Faz o cálculo da área do triângulo utilizando a função do módulo de utilidades
        resultadoTriangulo = utilidades.calcular_area_triangulo(base, altura)
        
        print(f"Área do Triângulo: {resultadoTriangulo} cm²")

    else:
        print("Opção Inválida!")

    continuar = input("Deseja continuar (S/N): ")

    if (continuar.upper() == "N"): break