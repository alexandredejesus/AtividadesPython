def main():
    notas = []  # Lista para armazenar as notas válidas
    
    print("Registro de Notas da Turma")
    print("Digite 'fim' para encerrar e calcular a média\n")
    
    while True:
        entrada = input("Digite uma nota entre 0 e 10: ").strip().lower()
        
        # Verifica se o usuário quer encerrar
        if entrada == "fim":
            if len(notas) == 0:
                print("\nNenhuma nota foi registrada!")
                return
            break
        
        try:
            # Tenta converter para número
            nota = float(entrada)
            
            # Verifica se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"✓ Nota {nota} registrada com sucesso!")
            else:
                print("Erro: A nota deve estar entre 0 e 10!\n")
                
        except ValueError:
            print("Erro: Digite apenas números ou 'fim' para encerrar!\n")
    
    # Cálculos finais
    total_notas = len(notas)
    media = sum(notas) / total_notas
    
    # Exibe resultados
    print("\n" + "=" * 50)
    print("RESULTADOS FINAIS".center(50))
    print("=" * 50)
    print(f"→ Total de notas válidas registradas: {total_notas}")
    print(f"→ Média da turma: {media:.2f}")
    print("=" * 50)

if __name__ == "__main__":
    main()