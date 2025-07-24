nome = "Camiseta"
preco = 50.00
desconto_percentual = 20

valor_desconto = preco * desconto_percentual / 100
preco_final = preco - valor_desconto

print(f"Produto: {nome}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")