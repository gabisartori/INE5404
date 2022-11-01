from classes import *

def melhor(carta1, carta2):
    if carta1.manilha and not carta2.manilha: return True
    if carta2.manilha and not carta1.manilha: return False
    if carta1.manilha and carta2.manilha:
        if carta1.numero != '7' and carta2.numero != '7': return carta1.naipe == 'espadas'        
        return carta1.naipe == 'espadas'
    return carta1.naipe > carta2.naipe


deck = Deck()
deck.embaralhar()

j1 = Jogador('Juan')
j2 = Jogador('Pedro')

jogadores = [j1, j2]

for _ in range(3):
    for jogador in jogadores:
        jogador.receber_carta(deck.pop())


c2 = Carta(1, 'espadas')
c1 = Carta(1, 'paus')
print(melhor(c1, c2))