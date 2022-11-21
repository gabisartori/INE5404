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
            True
        ]
        self.forca = 9 - self.status.index(True)
        if self.forca == 9:
            self.forca *= 100_000_000_000
        elif self.forca == 8:
            self.forca *= 10_000_000_000
            self.forca += max([carta.numero for carta in self.cartas]) * 1_000_000_000
        elif self.forca == 7:
            self.forca *= 1_000_000_000
            self.forca += self.cartas[2].numero * 100_000_000
        elif self.forca == 6:
            self.forca *= 100_000_000
            self.forca += self.cartas[2].numero * 10_000_000
            self.forca += self.cartas[3].numero * 1_000_000
        elif self.forca == 5:
            self.forca *= 1_000_000
            self.forca += max([carta.numero for carta in self.cartas]) * 100_000
        elif self.forca == 4:
            self.forca *= 100_000
            self.forca += max([carta.numero for carta in self.cartas]) * 10_000
        elif self.forca == 3:
            self.forca *= 1_000
            trio = [carta.numero for carta in self.cartas if self.cartas.count(carta) == 3][0]
            self.forca +=  trio*1000 + max([carta.numero for carta in self.cartas if carta.numero != trio]) * 100+ min([carta.numero for carta in self.cartas if carta.numero != trio])*10
        elif self.forca == 2:
            self.forca *= 1_000
            dupla = [carta.numero for carta in self.cartas if self.cartas.count(carta) == 2][0]
            outra_dupla = [carta.numero for carta in self.cartas if self.cartas.count(carta) == 2 and carta.numero != dupla][0]
            self.forca += dupla * 100 + outra_dupla*10 + [carta.numero for carta in self.cartas if carta.numero != dupla and carta.numero != outra_dupla][0]
        elif self.forca == 1:
            self.forca *= 100
            dupla = [carta.numero for carta in self.cartas if self.cartas.count(carta) == 2][0]
            self.forca += max([carta.numero for carta in self.cartas if carta.numero != dupla]) * 10
        else:
            self.forca *= 10
            self.forca += max([carta.numero for carta in self.cartas])


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
