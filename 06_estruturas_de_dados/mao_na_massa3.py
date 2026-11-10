## 🛠️ Prática do Aluno (Mão na Massa)
#Crie um dicionário representando um veículo com as chaves
#  `"marca"`, `"modelo"` e `"ano"`. Imprima cada chave e seu respectivo
#  valor usando o método `.items()` em um laço `for`.

veiculo = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2026
}

for chave, valor in veiculo.items():
    print(f"chave: {chave} -> valor: {valor}")