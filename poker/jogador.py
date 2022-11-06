class Jogador:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.cartas = []
        self.banco = 1000
        self.valor_aposta = 0
    
    def receber_carta(self, carta):
        self.cartas.append(carta)

    def aposta(self, valor, mesa):

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
            return 0

    def cobrir(self, valor):
        if self.banco >= valor:
            self.banco -= valor
            return valor
        else:
            # All-in
            temp = self.banco
            self.banco = 0
            return temp

    
    def cobrar(self, valor, mesa):
        choice = False
        if choice: return self.cobrir(valor)
        else:
            mesa.jogadores_ativos.remove(self)
            return False

    def receber(self, valor):
        self.banco += valor
    