from cartas import Deck

class Mesa:
    def __init__(self, jogadores) -> None:
        self.cartas = []
        self.jogadores = jogadores
        self.jogadores_ativos = []
        self.montante = 0
        self.valor_a_cobrar = 100
    
    def __str__(self):
        coisa = ''
        for carta in self.cartas:
            coisa += str(carta) + '\n'
        return coisa

    def receber_carta(self, carta):
        self.cartas.append(carta)
    
    def rodada_aposta(self):
        # resetar valor a cobrar
        self.valor_a_cobrar = 0 # Jogadores podem apenas bater na mesa

        # Jogadores começam sem apostar nada
        for jogador in self.jogadores: jogador.valor_aposta = 0
        print([jogador.nome for jogador in self.jogadores_ativos])
        # Rodada
        while True:
            # Percorrendo os jogadores em ordem reversa para que, ao remover um jogador, o próximo não seja pulado
            for i in range(len(self.jogadores_ativos)-1, -1, -1):
                jogador = self.jogadores_ativos[i]
                print("="*20)
                print(jogador.nome, jogador.valor_aposta)
                print([str(carta) for carta in jogador.cartas])
                jogador.valor_aposta = jogador.aposta(self.valor_a_cobrar, self)
                print(jogador.nome, jogador.valor_aposta)

                # Caso o jogador aumente a aposta
                if jogador.valor_aposta > self.valor_a_cobrar:
                    self.valor_a_cobrar = jogador.valor_aposta
                if all([jogador.valor_aposta == self.valor_a_cobrar for jogador in self.jogadores_ativos]): break

            if all([jogador.valor_aposta == self.valor_a_cobrar for jogador in self.jogadores_ativos]):
                for jogador in self.jogadores: self.montante += jogador.valor_aposta
                print(self.montante)
                break


    def jogo(self):
        # Inicializando o jogo
        deck = Deck()
        deck.embaralhar()
        self.jogadores_ativos = self.jogadores.copy()
        self.montante = 0
        self.valor_a_cobrar = 100
        self.cartas = []
        for jogador in self.jogadores:
            jogador.cartas = []
            jogador.valor_aposta = 0
            jogador.mao = None
        
        # jogadores recebem duas cartas
        for _ in range(2):
            for jogador in self.jogadores_ativos:
                jogador.receber_carta(deck.pop())

        # rodada de aposta
        self.rodada_aposta()

        # São colocadas 3 cartas na mesa
        for _ in range(3): self.cartas.append(deck.pop())
        for carta in self.cartas: print(carta)
        
        # rodada de aposta
        self.rodada_aposta()

        # É colocada mais uma carta na mesa
        self.cartas.append(deck.pop())
        for carta in self.cartas: print(carta)

        # rodada de aposta
        self.rodada_aposta()

        # É colocada mais uma carta na mesa
        self.cartas.append(deck.pop())
        for carta in self.cartas: print(carta)

        # rodada de aposta
        self.rodada_aposta()

        # Showdown

        # Jogadores montam suas mãos
        for jogador in self.jogadores_ativos:
            jogador.montar_mao(self.cartas)
        
        # Jogadores são ordenados de acordo com a força de suas mãos
        self.jogadores_ativos.sort(key=lambda jogador: jogador.mao.forca, reverse=True)
        print([jogador.nome for jogador in self.jogadores_ativos])

        # Jogador com maior força recebe o montante
        self.jogares_ativos[0].receber_montante(self.montante)    