from jogador import Jogador
from mesa import Mesa
from cartas import Carta, Deck

# Create players
jogadores = []
for nome in ['João', 'Maria', 'Pedro', 'Ana']: jogadores.append(Jogador(nome))

# Create a new table
mesa = Mesa(jogadores)
while True:
    mesa.jogo()
    if input("Quer continuar? [S/N]").strip()[0] in 'Nn': break