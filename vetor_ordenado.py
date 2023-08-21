import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(capacidade, dtype=np.int32)
        # for i in range(self.valores.size):
        #     self.valores[i] = 0

    def imprime(self):
        if self.ultima_posicao == -1:
            print('Vetor Vazio!')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade Maxima atingida!')
            return

        posicao = self.ultima_posicao + 1
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                posicao = i
                break

        aux = self.ultima_posicao
        while aux >= posicao:
            self.valores[aux + 1] = self.valores[aux]
            aux -= 1
        self.valores[posicao] = valor
        self.ultima_posicao += 1


if __name__ == '__main__':

    vetor = VetorOrdenado(10)
    vetor.imprime()
    vetor.insere(6)
    vetor.imprime()
    vetor.insere(4)
    vetor.insere(3)
    vetor.insere(10)
    vetor.insere(5)
    vetor.imprime()
    vetor.insere(15)
    vetor.insere(1)
    vetor.insere(8)
    vetor.insere(22)
    vetor.insere(16)
    vetor.insere(99)
    vetor.imprime()
