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