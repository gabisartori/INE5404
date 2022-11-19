import tkinter as tk
from controller import Controller
from produto import Produto

class menu:
    def __init__(self) -> None:
        self.connect = Controller()
        self.root = tk.Tk()
        self.root.title("Supermercado")
        self.root.geometry("400x400")

    @staticmethod
    def clear(window):
        for child in window.winfo_children():
            child.destroy()

    def cadastrar(self):
        self.clear(self.root)
        tk.Label(self.root, text="Cadastrar").pack()

        tk.Label(self.root, text="Nome do produto").pack()
        nome = tk.Entry(self.root)
        nome.pack()

        tk.Label(self.root, text="Preço do produto").pack()
        preco = tk.Entry(self.root)
        preco.pack()

        tk.Label(self.root, text="Unidade").pack()
        unitario = tk.BooleanVar()
        tk.Checkbutton(self.root, variable=unitario, onvalue=True, offvalue=False).pack()

        tk.Button(self.root, text="Cadastrar produto", command=lambda: self.connect.add_product(Produto(nome.get(), float(preco.get()), unitario))).pack()

        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def listar(self):
        self.clear(self.root)
        tk.Label(self.root, text="Listar").pack()
        
        products = self.connect.get_products()
        for product in products:
            item = tk.Frame(self.root, height=2, bg="black")
            item.pack()
            tk.Label(self.root, text=f'{product.name} R${product.price:.2f}').pack(in_=item, side=tk.LEFT)
            tk.Button(self.root, text="Remover", command=lambda: self.connect.remove_product(product.id)).pack(in_=item, side=tk.RIGHT)

        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def buscar(self):
        self.clear(self.root)
        tk.Label(self.root, text="Buscar").pack()

        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def remover(self):
        self.clear(self.root)
        tk.Label(self.root, text="Remover").pack()

        tk.Label(self.root, text="Id ou nome do produto").pack()
        entry = tk.Entry(self.root)
        entry.pack()
        
        def test():
            code = entry.get()
            if code.isdigit():
                product = self.connect.get_product_by_id(int(code))
            else:
                product = self.connect.get_product_by_name(code)
        
            if type(product) == str:
                aviso = tk.Label(self.root, text=product)
                aviso.pack()
                aviso.after(3000, aviso.destroy)
            else:
                self.connect.remove_product(product.id)
                aviso = tk.Label(self.root, text="Produto removido com sucesso!")
                aviso.pack()

        tk.Button(self.root, text="Remover", command=test).pack()

        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def inicio(self):
        self.clear(self.root)
        tk.Button(self.root, text="Cadastrar Produto", command=self.cadastrar).pack()
        tk.Button(self.root, text="Listar Produtos", command=self.listar).pack()
        tk.Button(self.root, text="Buscar Produto", command=self.buscar).pack()
        tk.Button(self.root, text="Remover Produto", command=self.remover).pack()


    def run(self):
        self.inicio()
        self.root.mainloop()

coisa = menu()
coisa.run()