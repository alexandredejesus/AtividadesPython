import requests

print("Consulta de CEP - ViaCEP API")
print("=" * 30)

# Solicita o CEP ao usuário
cep = input("Digite o CEP (apenas números): ").strip()

# Verifica se o CEP tem 8 dígitos
if len(cep) != 8 or not cep.isdigit():
    print("\nErro: CEP inválido! Deve conter exatamente 8 dígitos numéricos.")
    exit()

# Monta a URL da API
url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    # Faz a requisição à API
    resposta = requests.get(url)
    
    # Verifica se houve erro na requisição HTTP
    resposta.raise_for_status()
    
    # Converte a resposta para JSON
    dados = resposta.json()
    
    # Verifica se o CEP foi encontrado
    if "erro" in dados:
        print("\nCEP não encontrado!")
    else:
        # Formata os dados para exibição
        cep_formatado = f"{dados['cep'][:5]}-{dados['cep'][5:]}"
        
        print("\nEndereço encontrado:")
        print("=" * 30)
        print(f"📍 CEP: {cep_formatado}")
        print(f"🏠 Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"🏡 Bairro: {dados.get('bairro', 'N/A')}")
        print(f"🏙️ Cidade: {dados.get('localidade', 'N/A')}")
        print(f"🌆 Estado: {dados.get('uf', 'N/A')}")
        print("=" * 30)

except requests.exceptions.HTTPError:
    print("\nErro: Falha na comunicação com a API ViaCEP!")
except requests.exceptions.ConnectionError:
    print("\nErro: Sem conexão com a internet!")
except requests.exceptions.Timeout:
    print("\nErro: Tempo de espera esgotado!")
except requests.exceptions.RequestException:
    print("\nErro: Problema inesperado ao acessar a API!")
except ValueError:
    print("\nErro: Resposta inválida da API!")