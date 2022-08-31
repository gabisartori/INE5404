from controller import Controller
from produto import Produto

connect = Controller()

class Menu():
    main_menu = '''[0] - Sair
[1] - Cadastrar produto
[2] - Listar produtos
[3] - Buscar produto
[4] - Remover produto
====================
'''


    def __init__(self) -> None:
        pass

    def run(self):
        print("Bem-vinde ao mercadinho do Python!")
        while True:
            print("O que você deseja fazer?")
            print(self.main_menu)
            option = input("Digite a opção desejada: ")
            if option == '0':
                break
            elif option == '1':
                nome = input("Digite o nome do produto: ")
                preco = int(input("Digite o preço do produto em centavos: "))
                unidade = input("Esse produto é vendido em unidades? [S/N]: ").strip().upper() == 'S'
                connect.add_product(Produto(nome, preco, unidade, 0))
            elif option == '2':
                for product in connect.get_products():
                    print(product)
            elif option == '3':
                code = input("Insira o nome ou o id do produto: ")
                if code.isdigit():
                    product = connect.get_product_by_id(int(code))
                else:
                    product = connect.get_product_by_name(code)
                
                print(product)

            elif option == '4':
                code = input("Insira o nome ou o id do produto: ")
                if code.isdigit():
                    product = connect.get_product_by_id(int(code))
                else:
                    product = connect.get_product_by_name(code)
                
                if type(product) == str:
                    print(product)
                else:
                    connect.remove_product(product.id)
                    print("Produto removido com sucesso!")


coiso = Menu()
coiso.run()