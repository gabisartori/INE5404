a = input("Insira um número entre 0 e 10: ")
valid = a.isnumeric() and int(a) >= 0 and int(a) <= 10
while not valid:
    print("Valor inválido")
    a = input("Insira um número entre 0 e 10: ")
    valid = a.isnumeric() and int(a) >= 0 and int(a) <= 10