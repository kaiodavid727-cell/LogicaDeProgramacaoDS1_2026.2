"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:

X = int(input(" digite um numero:"))
Y = int(input(" digite um numero maior que o anterior pulando 10 casa decimais:"))

inicio = min(X, Y)
fim = max(X, Y)

for i in range(inicio + 1, fim): 
    if i % 5 == 2 or i % 5 == 3:
        print(i) 