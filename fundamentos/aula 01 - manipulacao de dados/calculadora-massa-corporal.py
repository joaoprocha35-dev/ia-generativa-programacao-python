peso = float(input("Informe o peso (kg): "))
altura = float(input("Informe a altura (m): "))

imc = peso / (altura ** 2)
print(f"O IMC é: {imc:.2f}")