class Mesa:
    def __init__(self, jogadores) -> None:
        self.cartas = []
        self.jogadores = jogadores
        self.jogadores_ativos = []
        self.montante = 0
        self.valor_a_cobrar = 100
    
    def receber_carta(self, carta):
        self.cartas.append(carta)
    
    def rodada_aposta(self):
        while True:
            for jogador in self.jogadores_ativos:
                jogador.valor_aposta = jogador.aposta(self.valor_a_cobrar, self)
                self.montante += jogador.valor_aposta
            
            # break loop when all players have accepted the bet
            if all([jogador.valor_aposta == self.valor_a_cobrar for jogador in self.jogadores_ativos]):
                break

    def jogo(self, deck):
        self.montante = 0
        self.jogadores_ativos = self.jogadores.copy()
        self.valor_a_cobrar = 100

        for _ in range(3): self.cartas.append(deck.pop())
        for carta in self.cartas: print(carta)
        for jogador in self.jogadores:
            print(jogador.nome, jogador.cartas)
        self.jogadores_ativos = self.jogadores
        
        for jogador in self.jogadores_ativos:
            if jogador.cobrar(100, self): self.montante += 100