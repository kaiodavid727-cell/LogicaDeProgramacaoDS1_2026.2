"""
EXERCÍCIO 02: Tupla de Coordenadas e Imutabilidade
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma tupla com as cidades ("Tianguá", "São Benedito").
Tente alterar a posição 1 e use try-except para capturar o TypeError,
exibindo uma mensagem explicativa sobre imutabilidade.
"""

# TODO: Desenvolva o algoritmo abaixo:

cidades = ("Tianguá", "São Benedito")

try:
    cidades[1] = "Ubajara"
except TypeError as erro:
    print(f"Erro capturado: {erro}")
    print("\n[EXPLICAÇÃO]")
    print(f"Não foi possível alterar '{cidades[1]}' para 'Ubajara' porque as tuplas são **imutáveis**.")
    print("Isso significa que, uma vez criadas, seus elementos e sua estrutura não podem ser modificados, gerando o erro acima.")
