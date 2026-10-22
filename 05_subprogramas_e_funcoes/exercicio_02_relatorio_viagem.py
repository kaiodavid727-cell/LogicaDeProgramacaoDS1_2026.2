"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_klm, preco_combustivel):
    return (distancia_km / consumo_klm * preco_combustivel)

def calcular_custo_alimentaçao(qtd_pessoas, dias, diaria_alimentacao):
    return qtd_pessoas * dias * diaria_alimentacao

distacia = float(input("distacia (km): "))
consumo = float(input("consumo (km/l): "))
preco = float(input("preco combustivel R$:"))

pessoas = int(input("quantidade de pessoas: "))
dias = int(input("quantidade de dias:" ))
diaria = float(input("custo diaria de alimentaçao (R$): "))

transporte = calcular_custo_transporte(distacia, consumo, preco)
alimentacao = calcular_custo_alimentaçao(pessoas, dias, diaria)
total = transporte + alimentacao

print(f"\ncusto transporte: R$ {transporte:.2f}")
print(f"\ncusto alimentaçao: R$ {alimentacao:.2f}")
print(f"\ncusto total: R$ {total:.2f}")