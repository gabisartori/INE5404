from jogador import Jogador
from mesa import Mesa
from cartas import Carta, Deck

# Create a new game

# Create a new deck
deck = Deck()
deck.embaralhar()

# Create players
jogadores = []
for nome in ['João', 'Maria', 'Pedro', 'Ana']:
    jogadores.append(Jogador(nome))

# Create a new table
mesa = Mesa(jogadores)
print([jo.nome for jo in mesa.jogadores])
mesa.rodada_aposta()