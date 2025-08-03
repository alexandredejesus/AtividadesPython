import unicodedata

def normalizar_texto(texto):
    """
    Remove acentos, espaços, pontuações e converte para minúsculas
    """
    # Remove acentos e caracteres especiais
    texto_normalizado = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    
    # Remove espaços e pontuações, mantendo apenas letras e números
    texto_limpo = ''.join(c for c in texto_normalizado if c.isalnum())
    
    # Converte para minúsculas
    return texto_limpo.lower()

# Entrada do usuário
entrada = input("Digite uma palavra ou frase: ")

# Normaliza o texto
texto_normalizado = normalizar_texto(entrada)

# Verifica se é palíndromo (comparando com sua versão invertida)
if texto_normalizado == texto_normalizado[::-1]:
    print("\n✅ Sim, é um palíndromo!")
else:
    print("\n❌ Não, não é um palíndromo.")

# Opcional: Mostra o processo
print(f"\nTexto original: '{entrada}'")
print(f"Texto normalizado: '{texto_normalizado}'")
print(f"Texto invertido: '{texto_normalizado[::-1]}'")