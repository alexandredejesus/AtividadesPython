import csv

# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo CSV a ser lido (ex: dados.csv): ")

try:
    # Tenta abrir o arquivo para leitura
    with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo:
        # Cria um leitor CSV
        leitor_csv = csv.reader(arquivo)
        
        # Contador para numerar as linhas
        contador = 0
        
        # Lê e exibe cada linha do arquivo
        for linha in leitor_csv:
            contador += 1
            print(f"Linha {contador}: {linha}")

    # Confirmação de leitura
    print(f"\nTotal de linhas lidas: {contador}")

except FileNotFoundError:
    print(f"\nErro: O arquivo '{nome_arquivo}' não foi encontrado.")
except PermissionError:
    print("\nErro: Sem permissão para ler o arquivo.")
except Exception as erro:
    print(f"\nOcorreu um erro durante a leitura: {erro}")