"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
matriz_alunos = [
    ["paje", 8.0, 7.0 ],
    ["pixica", 9.0, 7.0],
    ["tabajara", 10.0, 6.5]
]

for aluno in matriz_alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]

    media = (nota1 + nota2) / 2

    situaçao = "Aprovado" if media >= 6.0 else "Prova Final"
    print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situaçao}")
