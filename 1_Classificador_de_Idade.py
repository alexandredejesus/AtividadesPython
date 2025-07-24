#Crie um programa que solicite a idade do usuário e classifique-o 
#em uma das seguintes categorias:

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")