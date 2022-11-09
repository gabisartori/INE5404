class Produto:
    def __init__(self, name: str, price: int, unitary: bool, id:int=0) -> None:
        self.name = name
        self.price = price
        self.unitary = unitary
        self.id = id
    
    def __str__(self) -> str:
        return f'''====================
id: {self.id}
Produto: {self.name} | Preço: R${self.price/100:.2f} {"unidade" if self.unitary else ""}
'''
