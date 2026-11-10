"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
cadastro = {
    "kaio": "estagiario",
    "betao": "vereador",
    "bruno trajano": "dono da ceasa"
}

for matricula, cargo in cadastro.items():
    print(f"matricula: {matricula} -> cargo: {cargo}")