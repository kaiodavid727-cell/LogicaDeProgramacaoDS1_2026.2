"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:
monitor = ["Ryan Mesquita Damasceno"]

monitor.append(input("digite o monitor: "))
monitor.append(input("digite o segundo monitor: "))

monitor[0] = "Ryan Mesquita Damasceno (ATUALIZADO)"
print(monitor)