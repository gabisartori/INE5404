nome = input("Insira seu nome: ")
senha = input("Insira sua senha: ")

while nome == senha:
    print("Nome e senha não podem ser iguais")
    nome = input("Insira seu nome: ")
    senha = input("Insira sua senha: ")

print("Nome e senha válidos")