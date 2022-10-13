def receber_dado(texto, tipo, condicao, erro):
    while True:
        try:
            dado = tipo(input(texto))
            if condicao(dado):
                return dado
            else:
                print(erro)
        except ValueError:
            print(erro)

def numero_valido(x):
    return x >= 0 and x <= 100

def main():
    nota = receber_dado("Digite uma nota: ", float, numero_valido, "Nota inválida")
    print(nota)

if __name__ == "__main__": main()