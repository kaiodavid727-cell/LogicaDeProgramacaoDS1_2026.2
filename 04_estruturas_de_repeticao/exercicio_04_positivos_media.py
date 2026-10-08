"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
quantidade_positivos = 0 
soma_positivos = 0.0

for i in range(1, 7):
    valor = float(input(f"digite o {i} valor: "))
    if valor > 0:
        quantidade_positivos += 1
        soma_positivos += valor

if quantidade_positivos > 0:
    media = soma_positivos / quantidade_positivos
    print(f"\na quantidade de valores positivos: {quantidade_positivos}")
    print(f"media dos valores postivos: {media:.1f}")
else:
    print(f"\nquantidade de valores positivos: 0")
    print("nao foi possivel calcular a media.")
    