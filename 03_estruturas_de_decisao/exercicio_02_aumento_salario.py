"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("Digite o salário:"))

if salario <= 400:
    percentual = 0.15
elif salario <= 800:
    percentual = 0.12
elif salario <= 1200:
    percentual = 0.10
elif salario <= 2000:
    percentual = 0.7
else: 
    percentual = 0.4

reajuste = salario * percentual / 100
novo_salario = salario + reajuste

print(f"salario novo: R$ {novo_salario:.2f}")
print(f"reajuste ganho: R$ {reajuste:.2f}")
print(f"Percentual aplicado: {percentual}%")