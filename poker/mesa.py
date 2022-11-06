class Mesa:
    def __init__(self, jogadores) -> None:
        self.cartas = []
        self.jogadores = jogadores
        self.jogadores_ativos = jogadores
        self.montante = 0
    
    def receber_carta(self, carta):
        self.cartas.append(carta)
    
    def jogo(self, deck):
        for _ in range(3): self.cartas.append(deck.pop())
        for carta in self.cartas: print(carta)
        for jogador in self.jogadores:
            print(jogador.nome, jogador.cartas)
        self.jogadores_ativos = self.jogadores
        
        for jogador in self.jogadores_ativos:
            if jogador.cobrar(100, self): self.montante += 100