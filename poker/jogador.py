from cartas import Mao, Carta

class Jogador:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.cartas = []
        self.banco = 1000
        self.valor_aposta = 0
        self.mao = None
    
    def receber_carta(self, carta: Carta) -> None:
        self.cartas.append(carta)

    def montar_mao(self, cartas_mesa: list[Carta]) -> None:
        cartas = ''
        while len(cartas) != 5:
            print(self.nome)
            cartas = input('Quais cartas você vai escolher? ')
        mao = []
        for carta in cartas:
            if carta.isnumeric():
                mao.append(cartas_mesa[int(carta)-1])
                continue
            if carta == 'a':
                mao.append(self.cartas[0])
                continue
            if carta == 'b':
                mao.append(self.cartas[1])
                continue
        if len(mao) == 5: self.mao =  Mao(mao)
        else: raise Exception('Mão inválida')
    
    def aposta(self, valor, mesa) -> int:

        # Recusar
        print('''[1] Cobrir
[2] Aumentar
[3] Recusar''')
        choice = int(input('Escolha uma opção: '))
        # Cobrir
        if choice == 1:
            return self.cobrir(valor) 
        
        # Aumentar
        if choice == 2:
            aumento = 100
            self.cobrir(valor + aumento)
            return valor + aumento

        # Recusar
        if choice == 3:
            mesa.jogadores_ativos.remove(self)
            return self.valor_aposta

    def cobrir(self, valor) -> int:
        if self.banco >= valor:
            self.banco -= valor
            return valor
        else:
            # All-in
            temp = self.banco
            self.banco = 0
            return temp

    def receber(self, valor) -> None:
        self.banco += valor
    