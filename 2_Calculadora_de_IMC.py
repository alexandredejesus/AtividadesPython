try:
    peso_str = input("Peso (kg): ").replace(',', '.')
    altura_str = input("Altura (ex: 170 cm ou 1.70 m): ").replace(',', '.')

    peso = float(peso_str)
    altura = float(altura_str)
    
    # Verifica se altura foi digitada em cm (valor > 2.5m é improvável)
    if altura > 2.5:
        altura /= 100  # Converte cm para m
        print("Altura interpretada como centímetros")
    
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classif = "Abaixo do peso"
    elif imc < 25:
        classif = "Peso normal"
    elif imc < 30:
        classif = "Sobrepeso"
    else:
        classif = "Obeso"
    
    print(f"IMC: {imc:.1f} - {classif}")

except ValueError:
    print("Erro: Valores inválidos! Use apenas números.")
except ZeroDivisionError:
    print("Erro: Altura não pode ser zero!")
except Exception as e:
    print(f"Erro inesperado: {str(e)}")