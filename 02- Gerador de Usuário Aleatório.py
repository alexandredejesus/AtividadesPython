import requests

# URL da API pública para gerar usuários aleatórios
API_URL = "https://randomuser.me/api/"

print("Obtendo dados de usuário aleatório...\n")

try:
    # Faz a requisição à API com timeout
    resposta = requests.get(API_URL, timeout=10)
    
    # Verifica se a requisição foi bem-sucedida
    resposta.raise_for_status()
    
    # Converte a resposta para JSON
    dados = resposta.json()
    
    # Verifica se há resultados
    if 'results' not in dados or not dados['results']:
        raise ValueError("Nenhum usuário encontrado na resposta da API")
    
    # Extrai as informações do usuário
    usuario = dados['results'][0]
    
    # CORREÇÃO: Nova estrutura da API
    nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    
    # Exibe as informações formatadas
    print("Informações do usuário:")
    print(f"📛 Nome: {nome_completo}")
    print(f"📧 E-mail: {email}")
    print(f"🌎 País: {pais}")

except requests.exceptions.HTTPError as http_err:
    print(f"\nErro HTTP ({http_err.response.status_code}): {http_err}")
    print("URL da requisição:", http_err.request.url)
except requests.exceptions.ConnectionError:
    print("\nErro: Falha na conexão com a internet!")
    print("Verifique sua conexão e tente novamente.")
except requests.exceptions.Timeout:
    print("\nErro: Tempo de espera esgotado!")
    print("A API não respondeu dentro do tempo limite (10 segundos).")
except requests.exceptions.RequestException as err:
    print(f"\nErro na requisição: {err}")
except (KeyError, IndexError) as e:
    print(f"\nErro: Estrutura inesperada nos dados da API! ({e})")
    print("A API pode ter mudado seu formato de resposta.")
    print("Resposta recebida:", dados)  # Mostra a resposta para depuração
except ValueError as ve:
    print(f"\nErro: {ve}")
except Exception as e:
    print(f"\nErro inesperado: {type(e).__name__} - {e}")