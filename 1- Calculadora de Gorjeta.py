def calcular_gorjeta():
    print("=" * 50)
    print("CALCULADORA DE GORJETA".center(50))
    print("=" * 50)
    
    while True:
        try:
            # Solicita o valor da conta
            valor_conta = float(input("Digite o valor total da conta (R$): ").replace(",", "."))
            
            # Valida o valor da conta
            if valor_conta <= 0:
                print("Erro: O valor da conta deve ser positivo!\n")
                continue
                
            break  # Sai do loop se o valor for válido
                
        except ValueError:
            print("Erro: Digite um valor numérico válido! (Ex: 150.50)\n")
    
    while True:
        try:
            # Solicita a porcentagem da gorjeta
            porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): ").replace(",", "."))
            
            # Valida a porcentagem
            if porcentagem <= 0:
                print("Erro: A porcentagem deve ser positiva!\n")
                continue
                
            break  # Sai do loop se a porcentagem for válida
                
        except ValueError:
            print("Erro: Digite um valor numérico válido! (Ex: 15)\n")
    
    # Cálculos
    valor_gorjeta = valor_conta * (porcentagem / 100)
    total_pagar = valor_conta + valor_gorjeta
    
    # Exibe resultados formatados
    print("\n" + "=" * 50)
    print("RESUMO DA CONTA".center(50))
    print("=" * 50)
    print(f"→ Valor da conta: R$ {valor_conta:.2f}")
    print(f"→ Porcentagem da gorjeta: {porcentagem:.0f}%")
    print(f"→ Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"→ Total a pagar: R$ {total_pagar:.2f}")
    print("=" * 50)

# Executa o programa
if __name__ == "__main__":
    calcular_gorjeta()