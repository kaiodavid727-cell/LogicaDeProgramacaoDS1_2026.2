"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
evidencias_suspeitas = ["notebook", "pen drive", "notebook", "celular", "pen drive", "documento" ]

itens_unicos = list(set(evidencias_suspeitas))

print("--- INVESTIGAÇÃO: ITENS ÚNICOS ---")
print(f"Lista original: {evidencias_suspeitas}")
print(f"Itens únicos extraidos: {itens_unicos}\n")

dados_suspeitos = {
    "nome": "Carlos Silva",
    "codinome": "Sombra",
    "status": "Sob vigilância "
}

print("--- INVESTIGAÇÃO: CONSULTA DE DADOS ---")

codinome = dados_suspeitos.get("codinome")
print(f"Codinome encontrado: {codinome}")

passaporte = dados_suspeitos.get("passaporte")
print(f"Número do passaporte: {passaporte} (Chave não encontrada, mas programa continua rodando!)")

localizacao = dados_suspeitos.get("ultima_localizacao", "destino desconhecido")
print(f"Última localização: {localizacao}")