#!/usr/bin/env python3
import random

class Humano:
    #atributos constantes
    # pernas = 2
    # bracos = 2
    # cabeca = 1
    _PI = 3,1415

# Metodos mágicos
    def __init__(self, nome): # metodo construtor
        # atributos do objeto
        self.pernas = 2
        self.bracos = 2
        self.nome = nome
        self.saldo = 0

# metodo
    def acidente(self):
        self.pernas -= 1
    def saldo_bancario(self):
        if self.pernas < 2 and self.nome == 'Carlos':
            self.saldo -= 10000
            print('Você está de ferias permanentes')
            if random.randint(1,10) == 9:
                self.saldo *= -1
        else:
            print('Você não é o Carlos')
            self.saldo += 10000
            print(f'Você agora tem {self.saldo}')

carlos = Humano('Carlos') # criando um objeto
# carlos._PI = 4
# print(carlos._PI)
# print(Humano._PI)
# carlos.pernas #acessando um atributo
# print(carlos.pernas) # exibindo um atributo
# carlos.pernas = 1
# print(carlos.pernas)
print(carlos.pernas)
carlos.acidente()
print(carlos.pernas)
carlos.saldo_bancario()
print(carlos.saldo)