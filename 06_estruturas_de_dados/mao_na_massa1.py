## 🛠️ Prática do Aluno (Mão na Massa)
#Crie uma lista vazia chamada `carrinho_compras`.
#  Solicite ao usuário 3 produtos para adicionar ao carrinho usando `.append()`.
#  Ao final, imprima a lista ordenada em ordem alfabética com `.sort()`.

carrinho_compras = []

for i in range(3):
    produto = input(f"digite o nome d produto {i+1}:")
    carrinho_compras.append(produto)

    carrinho_compras.sort()

    print("\nCarrinho de compras:")
    print(carrinho_compras)