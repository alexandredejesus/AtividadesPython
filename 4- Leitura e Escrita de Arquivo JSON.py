import json

# Cria um dicionário com dados de uma pessoa
pessoa = {
    "nome": "Carlos Silva",
    "idade": 35,
    "cidade": "Porto Alegre",
    "profissao": "Engenheiro"
}

# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")

try:
    # Salva os dados no arquivo JSON
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    print(f"\nDados salvos com sucesso em '{nome_arquivo}'!")

    # Lê os dados do mesmo arquivo
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)
    
    # Exibe os dados lidos
    print("\nDados lidos do arquivo:")
    for chave, valor in dados_lidos.items():
        print(f"{chave.capitalize()}: {valor}")

except PermissionError:
    print("\nErro: Sem permissão para acessar o arquivo.")
except FileNotFoundError:
    print("\nErro: Arquivo não encontrado - verifique o caminho.")
except json.JSONDecodeError:
    print("\nErro: Problema na formatação do arquivo JSON.")
except Exception as erro:
    print(f"\nOcorreu um erro inesperado: {erro}")