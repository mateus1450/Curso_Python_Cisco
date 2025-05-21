# Entrada do usuário
blocos = int(input("Digite o número total de blocos: "))

altura = 0
camada = 1

# Enquanto houver blocos suficientes para formar a próxima camada
while blocos >= camada:
    blocos -= camada
    altura += 1
    camada += 1
print(f"A altura da pirâmide construída é: {altura}")