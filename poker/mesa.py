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
        # Jogadores começam sem apostar nada
        self.jogadores_ativos = self.jogadores.copy()
        for jogador in self.jogadores: jogador.valor_aposta = 0
        
        # Rodada
        while True:
            for jogador in self.jogadores_ativos:
                print(jogador.nome, jogador.valor_aposta)
                jogador.valor_aposta = jogador.aposta(self.valor_a_cobrar, self)
                print(jogador.nome, jogador.valor_aposta)

                # Caso o jogador aumente a aposta
                if jogador.valor_aposta > self.valor_a_cobrar:
                    self.valor_a_cobrar = jogador.valor_aposta
                
            
                # break loop when all players have accepted the bet
                if all([jogador.valor_aposta == self.valor_a_cobrar for jogador in self.jogadores_ativos]):
                    break
            if all([jogador.valor_aposta == self.valor_a_cobrar for jogador in self.jogadores_ativos]):
                for jogador in self.jogadores: self.montante += jogador.valor_aposta
                print(self.montante)
                break


    def jogo(self, deck):
        self.montante = 0
        self.jogadores_ativos = self.jogadores.copy()
        self.valor_a_cobrar = 100

        for _ in range(3): self.cartas.append(deck.pop())
        for carta in self.cartas: print(carta)
        for jogador in self.jogadores:
            print(jogador.nome, jogador.cartas)