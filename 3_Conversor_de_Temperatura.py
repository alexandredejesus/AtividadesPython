temp = float(input("Temperatura: ").replace(',', '.'))
origem = input("De (C/F/K): ").upper()
destino = input("Para (C/F/K): ").upper()

# Converte tudo para Celsius primeiro
if origem == "F":
    c = (temp - 32) * 5/9
elif origem == "K":
    c = temp - 273.15
else:  # Já é Celsius
    c = temp

# Converte para unidade desejada
if destino == "F":
    res = c * 9/5 + 32
elif destino == "K":
    res = c + 273.15
else:  # Celsius
    res = c

print(f"{temp}°{origem} = {res:.1f}°{destino}")