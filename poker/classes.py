import random

# Texas holdem poker game

class Carta:
    def __init__(self, numero, naipe) -> None:
        self.numero = \
            'A' if numero == 1 \
                else 'J' if numero == 11 \
                else 'Q' if numero == 12 \
                else 'K' if numero == 13 \
                else str(numero)
        self.naipe = naipe

    def __str__(self) -> str:
        return f'{self.numero} de {self.naipe}'

class Deck:
    def __init__(self) -> None:
        self.cartas = []
        for numero in range(1, 14):
            for naipe in ['Ouros', 'Copas', 'Paus', 'Espadas']:
                carta = Carta(numero, naipe)
                self.cartas.append(carta)
            
    def embaralhar(self):
        random.shuffle(self.cartas)

    def pop(self):
        return self.cartas.pop()

class Jogador:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.cartas = []
    
    def receber_carta(self, carta):
        self.cartas.append(carta)

class Jogo:
    def __init__(self, jogadores) -> None:
        self.jogadores = jogadores
        self.deck = Deck()
        self.deck.embaralhar()

    def distribuir_cartas(self):
        for _ in range(2):
            for jogador in self.jogadores: jogador.receber_carta(self.deck.pop())

    def __str__(self) -> str:
        resultado = ''
        for jogador in self.jogadores:
            resultado += f'{jogador.nome}: {jogador.cartas}'
        return resultado
    