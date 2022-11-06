import random

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
