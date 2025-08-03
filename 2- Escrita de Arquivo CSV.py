import csv

# Dados fictícios de pessoas (nome, idade, cidade)
pessoas = [
    ["João Silva", 28, "São Paulo"],
    ["Maria Oliveira", 34, "Rio de Janeiro"],
    ["Carlos Souza", 22, "Belo Horizonte"],
    ["Ana Costa", 45, "Salvador"]
]

# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo CSV a ser criado (ex: pessoas.csv): ")

try:
    # Cria e abre o arquivo no modo de escrita
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        # Cria um objeto escritor CSV
        escritor_csv = csv.writer(arquivo)
        
        # Escreve o cabeçalho
        escritor_csv.writerow(["Nome", "Idade", "Cidade"])
        
        # Escreve os dados das pessoas
        escritor_csv.writerows(pessoas)
    
    # Confirmação de sucesso
    print(f"\nArquivo '{nome_arquivo}' criado com sucesso!")
    print(f"Foram salvas {len(pessoas)} pessoas no arquivo.")

except PermissionError:
    print("\nErro: Permissão negada para criar o arquivo. Talvez o arquivo esteja aberto em outro programa.")
except Exception as erro:
    print(f"\nOcorreu um erro ao criar o arquivo: {erro}")