print("Hello, World!")
print(5 + 2)
produto1 = 5
print(produto1)
produto2 = 2000
print(produto1 + produto2)

# ---
print()

nome_do_produto1 = "Macarrão"
nome_do_produto2 = "Celular"
nome_do_produto3 = "Bala"
print(
    nome_do_produto1 + " " +
    nome_do_produto2 + " " +
    nome_do_produto3
)

# ---
print()

amigos = 5
aluguel = 1000
supermercado = 500
carro = 400
total = aluguel + supermercado + carro
print(total)
aluguel = 900
print(total)

# ---
print()

aluguel = aluguel - 100
print(aluguel)
total_de_carros = carro * 2
total = aluguel + total_de_carros + supermercado
total_por_pessoa = total / amigos
print(total_por_pessoa)

#---
print()

print(type(True).__name__)
print(type(10).__name__)
print(type(10.0).__name__)
print(type("Hello").__name__)