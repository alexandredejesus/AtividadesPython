'''4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.'''

Nome_do_produto= "Cadeira Infantil"
Preco_unitario= 12.40
Quantidade= 3

Preco_total = Preco_unitario * Quantidade

print("\n----- RESUMO DA COMPRA -----")
print(f"{Quantidade}x {Nome_do_produto} - R$ {Preco_unitario:.2f} cada")
print(f"TOTAL: R$ {Preco_total:.2f}")