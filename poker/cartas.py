import random

class Carta:
    def __init__(self, numero, naipe) -> None:
        self.numero = numero
        self.naipe = naipe

    def __str__(self) -> str:
        simbolo = \
            'A' if self.numero == 1 \
                else 'J' if self.numero == 11 \
                else 'Q' if self.numero == 12 \
                else 'K' if self.numero == 13 \
                else str(self.numero)
        return f'{simbolo} de {self.naipe}'

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

class Mao:
    def __init__(self, cartas: list[Carta]) -> None:
        self.cartas = sorted(cartas, key=lambda carta: carta.numero)
        self.status = [
            self.is_royal_flush(),
            self.is_straight_flush(),
            self.is_quadra(),
            self.is_full_house(),
            self.is_flush(),
            self.is_straight(),
            self.is_trinca(),
            self.is_dois_pares(),
            self.is_par(),
            self.cartas[-1].numero
        ]

    def is_royal_flush(self):
        return all([carta.naipe == self.cartas[0].naipe for carta in self.cartas]) and [carta.numero for carta in self.cartas] == [1, 10, 11, 12, 13]

    def is_straight_flush(self):
        return all([carta.naipe == self.cartas[0].naipe for carta in self.cartas]) and self.is_straight()
    
    def is_quadra(self):
        return self.is_n_of_a_kind(4)
    
    def is_full_house(self):
        return self.is_n_of_a_kind(3, 2)
    
    def is_flush(self):
        return all([carta.naipe == self.cartas[0].naipe for carta in self.cartas])
    
    def is_straight(self):
        return all([self.cartas[i].numero == self.cartas[i+1].numero for i in range(4)]) or [carta.numero for carta in self.cartas] == [1, 10, 11, 12, 13]

    def is_trinca(self):
        return self.is_n_of_a_kind(3)
    
    def is_dois_pares(self):
        return self.is_n_of_a_kind(2, 2)
    
    def is_par(self):
        return self.is_n_of_a_kind(2)
    
    def is_n_of_a_kind(self, n, m=1):
        numeros = [carta.numero for carta in self.cartas]
        for numero in numeros:
            if numeros.count(numero) == n:
                numeros.remove(numero)
                if m == 1:
                    return True
                else:
                    return self.is_n_of_a_kind(n, m-1)
        return False

    def __str__(self) -> str:
        coisa = ''
        for carta in self.cartas:
            coisa += str(carta) + '\n'
