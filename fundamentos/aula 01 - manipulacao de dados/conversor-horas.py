#Solicita o valor em horas ao usuário
horas = int(input("Digite o valor em horas:"))

#Converte o valor em horas para minutos e segundos
minutos = horas * 60
segundos = minutos * 60

#Saída dos valores convertidos
print(f"Horas informadas: {horas}")
print(f"O valor em minutos é: {minutos}")
print(f"O valor em segundos é: {segundos}")