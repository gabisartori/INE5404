nome = input("Insira teu nome: ")
idade = input("Insira tua idade: ")
salario = input("Insira teu salário: ")
sexo = input("Insira teu sexo [M/F] ")
print('''S - Solteiro
C - Casado
V - Viúvo
D - Divorciado''')
estado = input("Insira teu estado civil: [S/C/V/D] ")

nome_valido = len(nome) > 3
idade_valida = idade.isnumeric() and int(idade) >= 0 and int(idade) <= 150
salario_valido = salario.isnumeric() and int(salario) >= 0
sexo_valido = sexo == "M" or sexo == "F"
estado_valido = estado == "S" or estado == "C" or estado == "V" or estado == "D"

print("Nome válido" if nome_valido else "Nome inválido")
print("Idade válida" if idade_valida else "Idade inválida")
print("Salário válido" if salario_valido else "Salário inválido")
print("Sexo válido" if sexo_valido else "Sexo inválido")
print("Estado válido" if estado_valido else "Estado inválido")
