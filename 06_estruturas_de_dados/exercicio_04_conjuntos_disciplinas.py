"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web = {"kaio", "pixica", "betao", "tabajara"}
alunos_banco = {"kaio", "pixica", "paje", "andin"}

interseçao = alunos_web & alunos_banco
print(f"interseçao(&): {interseçao}")

diferenca = alunos_web - alunos_banco
print(f"Diferença (-): {diferenca}")