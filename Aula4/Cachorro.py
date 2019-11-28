class Animal:
    nome = 'Animal'
    cabeca = 1

    def __init__(self):
        pass

    def viver(self):
        print('Estou vivo!!')

class Cachorro(Animal):
    '''Abstração de um cachorro

Cria um cachorro baseado em conceitos definidos em sala'''
    _DNA = 'Cachorro'

    def __init__(self, nome, idade, cor, raca='Vira-lata', porte='Médio', lingua=True):
        # Atributos Obrigatorios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.lingua = lingua # Valores únicos com True/False
        # Atributos padrão
        self.patas = 4
        self.orelha = 2
        self.focinho = True # Valores únicos com True/False
        #self.lingua = True # Valores únicos com True/False
        self.olhos = 2
        self.rabo = True # Valores únicos com True/False

        print(f'Cachorro {nome}, Construido com sucesso, possui {self.idade} anos,é da raça {self.raca}')
    
    # O que faz - Metodos
    def latir(self):
        #if self.lingua:
        if self.lingua == True:
            print('Au Au Au')
        else:
            print(f'{self.nome} não pode latir pois não tem lingua!')

    def comer(self):
        print('Comendo...')
    
    def cagar(self):
        print('Cagando.....')

    def dormir(self):
        print('Dormindo...')
        
    def cheirar(self):
        if self.focinho:
            print('Cheirando...')

    def __del__(self):
        print(f'Descanse em paz {self.nome}')

    def __str__(self):
        return 'Constroi um cachorro'