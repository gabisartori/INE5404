from classes import *

# Create a new game

# Create a new deck
deck = Deck()
deck.embaralhar()

# Create playerS
jogadores = []
for nome in ['João', 'Maria', 'Pedro', 'Ana']:
    jogadores.append(Jogador(nome))

# Deal cards
for _ in range(2):
    for jogador in jogadores:
        jogador.receber_carta(deck.pop())

# First round