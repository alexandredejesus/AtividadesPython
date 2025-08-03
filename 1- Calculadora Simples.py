while True:
    try:
        # Solicita os números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        
        # Realiza a operação correspondente
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            # Verifica divisão por zero
            if num2 == 0:
                print("\nErro: Divisão por zero não é permitida!")
                continue  # Volta ao início do loop
            resultado = num1 / num2
        else:
            print("\nErro: Operação inválida! Use apenas +, -, * ou /")
            continue  # Volta ao início do loop
        
        # Se chegou até aqui, tudo deu certo
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}")
        break  # Sai do loop
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos!\n")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}\n")