def calcular_desconto():
    print("=" * 50)
    print("CALCULADORA DE DESCONTO".center(50))
    print("=" * 50)
    
    while True:
        try:
            # Solicita o preço original
            preco = float(input("Digite o preço original do produto (R$): ").replace(",", "."))
            
            # Valida o preço
            if preco <= 0:
                print("Erro: O preço deve ser um valor positivo!\n")
                continue
                
            break  # Sai do loop se o valor for válido
                
        except ValueError:
            print("Erro: Digite um valor numérico válido! (Ex: 150.50)\n")
    
    while True:
        try:
            # Solicita o percentual de desconto
            desconto = float(input("Digite o percentual de desconto (%): ").replace(",", "."))
            
            # Valida o desconto
            if desconto < 0 or desconto > 100:
                print("Erro: O desconto deve estar entre 0% e 100%!\n")
                continue
                
            break  # Sai do loop se o desconto for válido
                
        except ValueError:
            print("Erro: Digite um valor numérico válido! (Ex: 15)\n")
    
    # Cálculos
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    
    # Exibe resultados formatados
    print("\n" + "=" * 50)
    print("RESUMO DA COMPRA".center(50))
    print("=" * 50)
    print(f"→ Preço original: R$ {preco:.2f}")
    print(f"→ Desconto aplicado: {desconto:.2f}%")
    print(f"→ Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"→ Preço final: R$ {preco_final:.2f}")
    print("=" * 50)

# Executa o programa
if __name__ == "__main__":
    calcular_desconto()