import numpy as np

# Inicialize uma lista vazia para armazenar os números
numeros = []

# loop para pegar os numeros das arry
while True:
    try:
        numero = float(input("Digite um número (ou digite '0' para parar): "))
        if numero == 0:
            break  # Sai do loop se o usuário digitar '0'
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

# Converta a lista de números em um array NumPy
array_numeros = np.array(numeros)

# Agora, você pode usar a variável "array_numeros" para acessar os valores

# Solicitar ao usuário um índice entre 0 e 10
indice = int(input("Digite um número entre 0 e 10 para acessar o valor correspondente: "))

if 0 <= indice < 10:
    if indice < len(array_numeros):
        valor = array_numeros[indice]
        print(f"O valor no índice {indice} é: {valor}")
    else:
        print("O índice está fora do alcance do array.")
else:
    print("Por favor, digite um número entre 0 e 10.")
