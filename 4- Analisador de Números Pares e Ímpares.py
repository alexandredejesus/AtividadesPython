print("Classificador de Números Pares e Ímpares")
print("Digite 'fim' para encerrar e ver os resultados\n")

# Contadores
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro: ").strip().lower()
    
    # Verifica se o usuário quer encerrar
    if entrada == "fim":
        break
    
    try:
        # Tenta converter para inteiro
        numero = int(entrada)
        
        # Verifica se é par ou ímpar
        if numero % 2 == 0:
            print(f"→ {numero} é PAR")
            pares += 1
        else:
            print(f"→ {numero} é ÍMPAR")
            impares += 1
            
    except ValueError:
        print("Erro: Digite apenas números inteiros ou 'fim' para encerrar!")

# Exibe resultados finais
print("\n" + "=" * 40)
print("RESULTADO FINAL".center(40))
print("=" * 40)
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
print(f"Total geral de números: {pares + impares}")
print("=" * 40)