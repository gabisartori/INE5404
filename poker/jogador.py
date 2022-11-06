class Jogador:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.cartas = []
        self.banco = 1000
    
    def receber_carta(self, carta):
        self.cartas.append(carta)

    def cobrir(self, valor):
        if self.banco >= valor:
            self.banco -= valor
        else:
            # All-in
            self.banco = 0
        return True
    
    def cobrar(self, valor, mesa):
        choice = False
        if choice: return self.cobrir(valor)
        else:
            mesa.jogadores_ativos.remove(self)
            return False

    def receber(self, valor):
        self.banco += valor
    