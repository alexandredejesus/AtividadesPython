from datetime import datetime

# Obtém o ano atual
ano_atual = datetime.now().year

print("Calculadora de Idade em Dias")
print("=" * 30)

# Solicita o ano de nascimento com validação
while True:
    try:
        nascimento = int(input("Digite seu ano de nascimento (4 dígitos): "))
        
        # Verifica se é um ano válido
        if nascimento < 1900 or nascimento > ano_atual:
            print(f"Erro: Ano deve estar entre 1900 e {ano_atual}!\n")
            continue
            
        break  # Sai do loop se o ano for válido
        
    except ValueError:
        print("Erro: Digite um ano válido (ex: 1990)!\n")

# Calcula a idade
idade_anos = ano_atual - nascimento
idade_dias = idade_anos * 365  # Desconsiderando anos bissextos

# Exibe o resultado
print("\n" + "=" * 30)
print(f"→ Ano atual: {ano_atual}")
print(f"→ Ano de nascimento: {nascimento}")
print(f"→ Idade em anos: {idade_anos}")
print(f"→ Idade em dias: {idade_dias} (aproximadamente)")
print("=" * 30)
print("Nota: O cálculo desconsidera anos bissextos e meses específicos")