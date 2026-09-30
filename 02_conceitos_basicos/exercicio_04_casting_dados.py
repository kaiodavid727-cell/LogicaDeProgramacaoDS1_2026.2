"""
EXERCÍCIO 04: Casting de Dados e Idade em 2026
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba do usuário o ano de nascimento como texto (str).
Converta essa entrada para inteiro (int) utilizando o conceito de casting
e calcule a idade que a pessoa completará até o final de 2026.
Imprima a idade calculada com uma mensagem personalizada.
"""

# TODO: Desenvolva o algoritmo abaixo:
data = str(input("digite o ano de nascimento"))
nome = str(input("digite seu nome"))
nascimento = int(data)
idade_usuario = 2026 - nascimento
print(f"sua idade ate final do ano sera :{idade_usuario}")