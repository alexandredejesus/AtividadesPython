print("Verificador de Força de Senha")
print("Digite 'sair' a qualquer momento para encerrar\n")

while True:
    senha = input("Digite uma senha para avaliação: ").strip()
    
    # Verifica se o usuário quer sair
    if senha.lower() == "sair":
        print("\nPrograma encerrado.")
        break
    
    # Verifica comprimento mínimo
    if len(senha) < 8:
        print("⚠️ Senha fraca! Deve ter pelo menos 8 caracteres.\n")
        continue
    
    # Verifica presença de números
    tem_numero = any(char.isdigit() for char in senha)
    
    if not tem_numero:
        print("⚠️ Senha fraca! Deve conter pelo menos um número.\n")
        continue
    
    # Se passou em todas as verificações
    print("✅ Senha forte! Atende aos critérios de segurança.\n")
    print("Programa encerrado.")
    break