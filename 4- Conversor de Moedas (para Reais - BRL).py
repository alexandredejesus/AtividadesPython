import requests
from datetime import datetime

def formatar_data(data_str):
    """Converte a string de data da API para formato amigável"""
    try:
        # Tenta converter para objeto datetime
        data_obj = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S")
        # Formata para português: DD/MM/AAAA HH:MM
        return data_obj.strftime("%d/%m/%Y %H:%M")
    except:
        return data_str  # Mantém o formato original se falhar

print("=" * 50)
print("COTAÇÃO DE MOEDAS EM TEMPO REAL".center(50))
print("=" * 50)
print("Moedas disponíveis: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY")
print("=" * 50)

# Solicita o código da moeda
codigo = input("Digite o código da moeda (ex: USD): ").strip().upper()

# Validação básica do código
if not codigo.isalpha() or len(codigo) != 3:
    print("\nErro: Código inválido! Deve ter 3 letras (ex: USD)")
    exit()

# Monta a URL da API
url = f"https://economia.awesomeapi.com.br/last/{codigo}-BRL"

try:
    # Faz a requisição à API
    resposta = requests.get(url, timeout=10)
    
    # Verifica se a resposta foi bem-sucedida
    resposta.raise_for_status()
    
    # Converte a resposta para JSON
    dados = resposta.json()
    
    # Verifica se a moeda existe na resposta
    chave = f"{codigo}BRL"
    if chave not in dados:
        print(f"\nErro: Moeda '{codigo}' não encontrada ou não suportada!")
        exit()
    
    # Extrai os dados relevantes
    moeda_info = dados[chave]
    nome = moeda_info['name']
    cotacao = float(moeda_info['bid'])
    maxima = float(moeda_info['high'])
    minima = float(moeda_info['low'])
    data_atualizacao = formatar_data(moeda_info['create_date'])
    
    # Exibe os resultados formatados
    print("\n" + "=" * 50)
    print(f"COTAÇÃO: {nome}".center(50))
    print("=" * 50)
    print(f"💵 Cotação atual: R$ {cotacao:.4f}")
    print(f"📈 Máxima do dia: R$ {maxima:.4f}")
    print(f"📉 Mínima do dia: R$ {minima:.4f}")
    print(f"🕒 Última atualização: {data_atualizacao}")
    print("=" * 50)

except requests.exceptions.HTTPError:
    print("\nErro: Falha na comunicação com o servidor de cotações!")
except requests.exceptions.ConnectionError:
    print("\nErro: Sem conexão com a internet!")
except requests.exceptions.Timeout:
    print("\nErro: Tempo de espera esgotado!")
except requests.exceptions.RequestException:
    print("\nErro: Problema inesperado ao acessar a API!")
except (KeyError, ValueError):
    print("\nErro: Dados recebidos em formato inesperado!")
except Exception as e:
    print(f"\nErro inesperado: {str(e)}")