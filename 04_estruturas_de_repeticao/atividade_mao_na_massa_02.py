soma = 0
print("digite os numeros que deseja somar (ou digite o numero 0 para parar): ")

while True:
    numero = int(input("digite um numero:"))

    if numero == 0:
        break
    soma += numero

    print(f"\na soma de todos os numeros digitados e: {soma}")