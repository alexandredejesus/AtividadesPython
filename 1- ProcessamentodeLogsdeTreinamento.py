import pandas as pd

# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo CSV (ex: logs_treinamento.csv): ")

try:
    # Tenta ler o arquivo CSV
    dados = pd.read_csv(nome_arquivo)
    
    # Verifica se a coluna necessária existe
    if 'tempo_execucao' not in dados:
        print("Erro: O arquivo não possui a coluna 'tempo_execucao'")
    else:
        # Calcula média e desvio padrão
        media = dados['tempo_execucao'].mean()
        desvio = dados['tempo_execucao'].std()
        
        # Exibe os resultados formatados
        print(f"\nMédia de tempo: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio:.2f} segundos")

except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio!")
except pd.errors.ParserError:
    print("Erro: Problema na formatação do arquivo CSV!")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")