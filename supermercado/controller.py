from produto import Produto

class Controller:
    def __init__(self):
        self.products = []
        self.id_counter = 0

    def get_product_by_name(self, name: str) -> Produto:
        for product in self.products:
            if product.name == name.lower():
                return product
        return 'Produto não encontrado'

    def get_product_by_id(self, id: int) -> Produto:
        for product in self.products:
            if product.id == id:
                return product
        return '''====================
Produto não encontrado
====================
'''
    
    def get_products(self) -> list[Produto]:
        return self.products
    
    def add_product(self, product: Produto) -> None:
        self.id_counter += 1
        product.id = self.id_counter
        self.products.append(product)

    def remove_product(self, id: int) -> None:
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                return
        return '''====================
Produto não encontrado
====================
'''
