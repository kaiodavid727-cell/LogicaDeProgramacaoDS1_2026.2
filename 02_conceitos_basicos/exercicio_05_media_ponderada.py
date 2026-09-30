"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:
nota1 = float(input("digite nota 1"))
nota2 = float(input("digite nota 2"))
nota3 = float(input("digite mota 3"))
peso1 = 3
peso2 = 4
peso3 = 6
media_final = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / 10
print (f"media final e: {media_final}")