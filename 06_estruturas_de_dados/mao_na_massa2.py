## 🛠️ Prática do Aluno (Mão na Massa)
#Crie uma matriz 2x2 contendo números inteiros e calcule a soma
#  de todos os 4 elementos utilizando dois laços `for` aninhados.

matriz = [
    [3, 12],
    [30, 40]
]

soma_total = 0

for linha in matriz:
    for elemento in linha:
        soma_total += elemento

print(f"a soma de todos 4 elementos e: {soma_total}")