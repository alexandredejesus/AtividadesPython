import random
import string

# Solicita o tamanho da senha
tamanho = int(input("Digite o tamanho da senha desejada (mínimo 4 caracteres): "))

# Verifica se o tamanho é suficiente
if tamanho < 4:
    print("Erro: O tamanho mínimo deve ser 4 caracteres!")
    exit()

# Define os conjuntos de caracteres
maiusculas = string.ascii_uppercase          # A-Z
minusculas = string.ascii_lowercase          # a-z
numeros = string.digits                      # 0-9
simbolos = "!@#$%&*"                         # Caracteres especiais

# Combina todos os caracteres
todos_caracteres = maiusculas + minusculas + numeros + simbolos

# Garante pelo menos um caractere de cada categoria
senha = [
    random.choice(maiusculas),
    random.choice(minusculas),
    random.choice(numeros),
    random.choice(simbolos)
]

# Preenche o restante da senha com caracteres aleatórios
for i in range(tamanho - 4):
    senha.append(random.choice(todos_caracteres))

# Embaralha os caracteres para maior aleatoriedade
random.shuffle(senha)

# Converte a lista em string
senha_gerada = ''.join(senha)

# Exibe o resultado
print("\nSenha gerada com segurança:")
print(f"🔒 {senha_gerada}")
print(f"Tamanho: {len(senha_gerada)} caracteres")