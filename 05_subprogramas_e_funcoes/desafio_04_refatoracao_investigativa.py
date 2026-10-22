"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:
def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    desconto = preco_base * (taxa_desc / 100)
    preco_com_desconto = preco_base - desconto

    imposto = preco_com_desconto * (taxa_imp / 100)
    preco_final = preco_com_desconto + imposto
    
    return preco_final

def exibir_relatorio_item(numero_item, preco_final):
    print("item numero:", numero_item)
    print("preço final: R$", preco_final)

resultado = calcular_preco_final(100, 15, 10)
exibir_relatorio_item(1, resultado)

