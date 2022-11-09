import tkinter as tk
from controller import Controller

class menu:
    def __init__(self) -> None:
        connect = Controller()
        self.root = tk.Tk()
        self.root.title("Supermercado")
        self.root.geometry("400x400")

    @staticmethod
    def clear(window):
        for child in window.winfo_children():
            child.destroy()

    def listar(self):
        self.clear(self.root)
        tk.Label(self.root, text="Listar").pack()

        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def buscar(self):
        self.clear(self.root)
        tk.Label(self.root, text="Buscar").pack()

        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def remover(self):
        self.clear(self.root)
        tk.Label(self.root, text="Remover").pack()
        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def inicio(self):
        self.clear(self.root)
        tk.Button(self.root, text="Cadastrar Produto", command=self.cadastrar).pack()
        tk.Button(self.root, text="Listar Produtos", command=self.listar).pack()
        tk.Button(self.root, text="Buscar Produto", command=self.buscar).pack()
        tk.Button(self.root, text="Remover Produto", command=self.remover).pack()

    def cadastrar(self):
        self.clear(self.root)
        tk.Label(self.root, text="Cadastrar").pack()
        tk.Button(self.root, text="Voltar", command=self.inicio).pack()

    def run(self):
        self.inicio()
        self.root.mainloop()

coisa = menu()
coisa.run()