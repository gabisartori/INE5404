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


# rodada de apostas

# três cartas são colocadas na mesa
for _ in range(3):
    mesa.receber_carta(deck.pop())
print(mesa)
# rodada de apostas

# uma carta é colocada na mesa
mesa.receber_carta(deck.pop())

# rodada de apostas

# uma carta é colocada na mesa
mesa.receber_carta(deck.pop())

# rodada de apostas

# jogadores mostram suas cartas

# jogador com a melhor mão ganha

# tudo é resetado


## rodada de apostas
# dealer paga a taxa inicial

# próximo jogador escolhe entre correr, cobrir ou aumentar

# se todos os jogadores cobrirem, a rodada termina